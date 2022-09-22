from typing import Optional

from pydantic import BaseModel


class ErpSchemaBase(BaseModel):
    id: Optional[int] = None
    ip: str
    login: str
    senha: str
    identificador: str
    vendor: str

    class Config:
        orm_mode = True
