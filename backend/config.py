import os

from dotenv import load_dotenv

load_dotenv(dotenv_path="./.env")


class Settings:
    JWT_SECRET = os.getenv("JWT_SECRET")
    IP_TOPSAPP = os.getenv("IP_TOPSAPP")
    ID_TOPSAPP = os.getenv("ID_TOPSAPP")
    USER_TOPSAPP = os.getenv("USER_TOPSAPP")
    PASS_TOPSAPP = os.getenv("PASS_TOPSAPP")
    USER_DB = os.getenv("USER_DB")
    PASS_DB = os.getenv("PASS_DB")
    SERV_DB = os.getenv("SERV_DB")
    PORT_DB = os.getenv("PORT_DB", 5432)
    DATABASE = os.getenv("DATABASE", "junosdb")
    SQLALCHEMY_DATABASE_URI = f"postgresql+asyncpg://{USER_DB}:{PASS_DB}@{SERV_DB}:{PORT_DB}/{DATABASE}"


setting = Settings()
