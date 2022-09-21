from typing import List

from database.database import Session
from database.deps import get_current_user, get_session
from fastapi import APIRouter, Depends, HTTPException, Response, status
from models.bras_model import BrasModel
from models.usuario_model import UsuarioModel
from schemas.bras_schema import BrasSchemaBase
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=BrasSchemaBase)
async def post_bras(
    bras: BrasSchemaBase,
    db: AsyncSession = Depends(get_session),
    usuario_logado: UsuarioModel = Depends(get_current_user),
):
    if not usuario_logado.eh_admin:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Não autorizado")

    novo_bras: BrasModel = BrasModel(
        ip=bras.ip,
        login=bras.login,
        senha=bras.senha,
        local=bras.local,
    )

    async with db as session:
        session.add(novo_bras)
        await session.commit()
        return novo_bras


@router.get("/", response_model=List[BrasSchemaBase])
async def get_bras(
    db: AsyncSession = Depends(get_session),
    usuario_logado: UsuarioModel = Depends(get_current_user),
):
    if not usuario_logado.eh_admin:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Não autorizado")

    async with db as session:
        query = select(BrasModel)
        result = await session.execute(query)
        bras: List[BrasSchemaBase] = result.scalars().unique().all()
        return bras


@router.get("/{bras_id}", response_model=BrasSchemaBase)
async def get_one_bras(
    bras_id: int, db: AsyncSession = Depends(get_session), usuario_logado: UsuarioModel = Depends(get_current_user)
):
    if not usuario_logado.eh_admin:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Não autorizado")

    async with db as session:
        query = select(BrasModel).filter(BrasModel.id == bras_id)
        result = await session.execute(query)
        bras: BrasSchemaBase = result.scalars().unique().one_or_none()

        if bras:
            return bras
        else:
            raise HTTPException(detail="Concentrador não encontrado", status_code=status.HTTP_404_NOT_FOUND)


@router.put("/{bras_id}", response_model=BrasSchemaBase, status_code=status.HTTP_202_ACCEPTED)
async def put_bras(
    bras_id: int,
    bras: BrasSchemaBase,
    db: AsyncSession = Depends(get_session),
    usuario_logado: UsuarioModel = Depends(get_current_user),
):

    if not usuario_logado.eh_admin:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Não autorizado")

    async with db as session:
        query = select(BrasModel).filter(BrasModel.id == bras_id)
        result = await session.execute(query)
        bras_update: BrasSchemaBase = result.scalars().unique().one_or_none()

        if bras_update:
            if bras.ip:
                bras_update.ip = bras.ip
            if bras.login:
                bras_update.login = bras.login
            if bras.senha:
                bras_update.senha = bras.senha
            if bras.local:
                bras_update.local = bras.local

            await session.commit()
            return bras_update

        else:
            raise HTTPException(detail="Concentrador não encontrado", status_code=status.HTTP_404_NOT_FOUND)


@router.delete("/{bras_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_bras(
    bras_id: int, db: AsyncSession = Depends(get_session), usuario_logado: UsuarioModel = Depends(get_current_user)
):

    if not usuario_logado.eh_admin:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Não autorizado")

    async with db as session:
        query = select(BrasModel).filter(BrasModel.id == bras_id)
        result = await session.execute(query)
        bras_del: BrasSchemaBase = result.scalars().unique().one_or_none()

        if bras_del:
            await session.delete(bras_del)
            await session.commit()
            return Response(status_code=status.HTTP_204_NO_CONTENT)

        else:
            raise HTTPException(detail="Concentrador não encontrado", status_code=status.HTTP_404_NOT_FOUND)
