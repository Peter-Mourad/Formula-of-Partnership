from fastapi import FastAPI, HTTPException
from fastapi.requests import Request
from fastapi.responses import PlainTextResponse
from fastapi.exceptions import RequestValidationError
from libformulaofpartnership.domain.utils import verify_token
from libformulaofpartnership.domain.user import get_user_by_code
from fastapi.responses import JSONResponse
from libformulaofpartnership import domain

app_params = {
    "title": "infosec-boilerplate API",
    "description": "Public API for infosec-boilerplate",
    "version": "0.1.0",
    "docs_url": "/swagger",
    "redoc_url": "/docs",
}

app = FastAPI(**app_params)


@app.exception_handler(AssertionError)
async def assert_error_handler(request: Request, exc: AssertionError):
    return PlainTextResponse(str(exc), status_code=400)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return PlainTextResponse(str(exc), status_code=400)


@app.middleware("http")
async def before_request(request: Request, call_next):
    if request.url.path.startswith("/dashboard"):
        partner_access_token_dev = request.cookies.get("partner_access_token_dev")
        partner_access_token = request.cookies.get("partner_access_token")
        request.state.user = None

        if partner_access_token_dev:
            user = get_user_by_code(partner_access_token_dev)
            if user:
                request.state.user = user

        elif partner_access_token:
            user = verify_token(partner_access_token)
            if user and user.get("is_approved"):
                request.state.user = user

        if not request.state.user:
            return JSONResponse(status_code=403, content="Forbidden Fruit")
        
    response = await call_next(request)
    return response


@app.get("/public/hc", status_code=200, tags=["system"])
def health_check():
    return "OK"


from appformulaofpartnership.urls import api_router

app.include_router(api_router)
