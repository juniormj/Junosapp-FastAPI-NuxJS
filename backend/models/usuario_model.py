# pylint: disable=import-error
from database.configs import settings
from sqlalchemy import Boolean, Column, Integer, String


class UsuarioModel(settings.DBBaseModel):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(256), nullable=True)
    sobrenome = Column(String(256), nullable=True)
    email = Column(String(256), index=True, nullable=True, unique=True)
    senha = Column(String(256), nullable=True)
    eh_admin = Column(Boolean, default=False)
