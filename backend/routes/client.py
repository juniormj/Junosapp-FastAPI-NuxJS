from database.deps import get_current_user
from fastapi import APIRouter, Depends, HTTPException, status
from lib.functions_bras import get_initial, get_logout, get_ports, get_total_client, get_vlan_total
from models.usuario_model import UsuarioModel

router = APIRouter()


@router.get("/{login}")
async def get_result(login: str, usuario_logado: UsuarioModel = Depends(get_current_user)):

    initial = await get_initial(login)
    if initial is not None:
        total_conn_vlan = await get_vlan_total(initial["vlan"], initial["ip_olt"])
        total_client = await get_total_client(initial["ip_olt"])
        ports = await get_ports(initial["ip"])
        return initial | total_conn_vlan | total_client | ports
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Usuário {login} não encontrado")


@router.get("/logoff/{login}/{ip_olt}")
async def logoff_user(login: str, ip_olt: str, usuario_logado: UsuarioModel = Depends(get_current_user)) -> dict:
    msg = await get_logout(login, ip_olt)
    return {"msg": msg}
