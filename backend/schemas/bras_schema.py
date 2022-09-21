from typing import Optional

from pydantic import BaseModel


class BrasSchemaBase(BaseModel):
    id: Optional[int] = None
    ip: str
    login: str
    senha: str
    local: str

    class Config:
        orm_mode = True
