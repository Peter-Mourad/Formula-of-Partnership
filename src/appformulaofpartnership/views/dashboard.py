from fastapi import APIRouter, Response, Request
from libformulaofpartnership.domain.registration import get_demo_user
from libformulaofpartnership.domain.sheet import read_from_url
from libformulaofpartnership.domain.product import get_partner_products, store_products
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from urllib.parse import urlparse
from fastapi.responses import JSONResponse

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/demo_dashboard", summary="Get default partner token", tags=["demo"])
def get_demo_dashboard(response: Response, request: Request):
    partner_access_token = get_demo_user()
    response = RedirectResponse(url="/dashboard")
    response.set_cookie(key="partner_access_token", value=partner_access_token)
    return response


@router.get("/dashboard")
def dashboard(request: Request):
    user = request.state.user
    if user["partner_code"].startswith("demo"):
        return templates.TemplateResponse(
            "demo_dashboard.html",
            {
                "request": request,
            }
        )
    products = get_partner_products(user["partner_code"])
    return templates.TemplateResponse(
        "dashboard.html",
        {"request": request, "products": products},
    )


@router.get("/dashboard/upload_products")
def upload_products(response: Response,request: Request, url: str):
    user = request.state.user
    if user["partner_code"].startswith("demo"):
        return JSONResponse(status_code=403, content="Forbidden Fruit")

    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    if domain != "docs.google.com":
        return JSONResponse(status_code=400, content="Invalid Url")

    data = read_from_url(url)

    store_products(data, user["partner_code"])
    response = RedirectResponse(url="/dashboard")
    return response

    
