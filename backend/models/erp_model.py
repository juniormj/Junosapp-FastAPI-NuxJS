# pylint: disable=import-error
from database.configs import settings
from sqlalchemy import Column, Integer, String


class ErpModel(settings.DBBaseModel):
    __tablename__ = "erps"

    id = Column(Integer, primary_key=True, autoincrement=True)
    ip = Column(String(16), nullable=True, unique=True)
    login = Column(String(100), nullable=True)
    senha = Column(String(80), nullable=True)
    identificador = Column(String(256), nullable=True)
    vendor = Column(String(256), nullable=True)
