from fastapi import APIRouter, Response, Request
from libformulaofpartnership.domain.registration import Partner
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.post('/register', summary='partner registeration', tags=['register'])
def post_register(partner: Partner):
    return partner.register()

@router.get('/', summary='partner registeration', tags=['register'])
def get_register(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})
