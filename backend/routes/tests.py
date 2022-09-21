from database.deps import get_current_user
from fastapi import APIRouter, Depends
from lib.functions_bras import get_extensives, get_ping_test, get_update_traffic
from models.usuario_model import UsuarioModel

router = APIRouter()


@router.get("/ping/{ip}")
async def test_ping(ip: str, usuario_logado: UsuarioModel = Depends(get_current_user)) -> dict:
    return await get_ping_test(ip)


@router.get("/extensive/{login}/{ip_olt}")
async def get_extensive(login: str, ip_olt: str, usuario_logado: UsuarioModel = Depends(get_current_user)) -> dict:
    return await get_extensives(login, ip_olt)


@router.get("/update/{interface}/{ip_olt}")
async def update(interface: str, ip_olt: str, usuario_logado: UsuarioModel = Depends(get_current_user)) -> dict:
    return await get_update_traffic(interface, ip_olt)
