from database.deps import get_current_user
from fastapi import APIRouter, Depends
from lib.utils import get_obter_clientes_servicos, get_obter_suporte_cliente
from models.usuario_model import UsuarioModel

router = APIRouter()


@router.get("/{login}")
async def get_clientes_servicos(login: str, usuario_logado: UsuarioModel = Depends(get_current_user)) -> dict:
    return await get_obter_clientes_servicos(login)


@router.get("/os/{id_cliente}")
async def get_suporte_cliente(id_cliente: int, usuario_logado: UsuarioModel = Depends(get_current_user)) -> dict:
    return await get_obter_suporte_cliente(id_cliente)
