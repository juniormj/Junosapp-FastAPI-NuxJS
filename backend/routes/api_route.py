from fastapi import APIRouter

from . import api_erp, bras, client, erp, logs, tests, usuario

api_route = APIRouter()

api_route.include_router(usuario.router, prefix="/usuarios", tags=["Usuários"])
api_route.include_router(bras.router, prefix="/bras", tags=["Concentradores"])
api_route.include_router(api_erp.router, prefix="/api_erps", tags=["API ERP"])
api_route.include_router(erp.router, prefix="/erps", tags=["ERP"])
api_route.include_router(client.router, prefix="/clients", tags=["Clientes"])
api_route.include_router(logs.router, prefix="/logs", tags=["Logs Radius"])
api_route.include_router(tests.router, prefix="/tests", tags=["Ferramenta de Testes"])
