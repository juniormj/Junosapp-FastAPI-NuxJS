# pylint: disable=import-error
from database.configs import settings
from sqlalchemy import Column, Integer, String


class BrasModel(settings.DBBaseModel):
    __tablename__ = "bras"

    id = Column(Integer, primary_key=True, autoincrement=True)
    ip = Column(String(16))
    login = Column(String(80))
    senha = Column(String(80))
    local = Column(String(150))
