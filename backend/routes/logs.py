from database.deps import get_current_user
from fastapi import APIRouter, Depends
from lib.utils import get_log, get_log_login
from models.usuario_model import UsuarioModel

router = APIRouter()


@router.get("/log")
async def get_logs(usuario_logado: UsuarioModel = Depends(get_current_user)) -> dict:
    return await get_log()


@router.get("/log/{login}")
async def get_log_by_login(login: str, usuario_logado: UsuarioModel = Depends(get_current_user)) -> dict:
    return await get_log_login(login)
