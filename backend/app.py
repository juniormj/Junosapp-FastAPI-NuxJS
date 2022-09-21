from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database.configs import settings
from routes import api_route

app = FastAPI(
    title="Documentação da API JunosAPP",
    description="Ferramenta com proposito a facilitar o suporte na empresa Atel Telecom",
)


app.include_router(api_route.api_route, prefix=settings.API_V1_STR)


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
