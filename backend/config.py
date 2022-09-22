import os

from dotenv import load_dotenv

load_dotenv(dotenv_path="./.env")


class Settings:
    USER_DB = os.getenv("USER_DB")
    PASS_DB = os.getenv("PASS_DB")
    SERV_DB = os.getenv("SERV_DB")
    PORT_DB = os.getenv("PORT_DB", 5432)
    DATABASE = os.getenv("DATABASE", "junosdb")
    SQLALCHEMY_DATABASE_URI = f"postgresql+asyncpg://{USER_DB}:{PASS_DB}@{SERV_DB}:{PORT_DB}/{DATABASE}"


setting = Settings()
