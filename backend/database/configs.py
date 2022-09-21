# pylint: disable=import-error
from config import setting
from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    DB_URL: str = setting.SQLALCHEMY_DATABASE_URI
    DBBaseModel = declarative_base()

    JWT_SECRET: str = setting.JWT_SECRET
    ALGORITHM: str = "HS256"
    # 60 minutos * 24 horas * 7 dias
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7

    class Config:
        case_sensitive = True


settings: Settings = Settings()
