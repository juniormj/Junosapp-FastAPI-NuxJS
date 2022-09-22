from typing import List

from database.deps import get_current_user, get_session
from fastapi import APIRouter, Depends, HTTPException, Response, status
from models.erp_model import ErpModel
from models.usuario_model import UsuarioModel
from schemas.erp_schema import ErpSchemaBase
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=ErpSchemaBase)
async def post_erp(
    bras: ErpSchemaBase,
    db: AsyncSession = Depends(get_session),
    usuario_logado: UsuarioModel = Depends(get_current_user),
):
    if not usuario_logado.eh_admin:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Não autorizado")

    novo_erp: ErpModel = ErpModel(
        ip=bras.ip,
        login=bras.login,
        senha=bras.senha,
        identificador=bras.identificador,
        vendor=bras.vendor,
    )

    async with db as session:
        session.add(novo_erp)
        await session.commit()
        return novo_erp


@router.get("/", response_model=List[ErpSchemaBase])
async def get_erps(
    db: AsyncSession = Depends(get_session),
    usuario_logado: UsuarioModel = Depends(get_current_user),
):
    if not usuario_logado.eh_admin:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Não autorizado")

    async with db as session:
        query = select(ErpModel)
        result = await session.execute(query)
        erp: List[ErpSchemaBase] = result.scalars().unique().all()
        return erp


@router.get("/{erp_id}", response_model=ErpSchemaBase)
async def get_erp(
    erp_id: int, db: AsyncSession = Depends(get_session), usuario_logado: UsuarioModel = Depends(get_current_user)
):
    if not usuario_logado.eh_admin:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Não autorizado")

    async with db as session:
        query = select(ErpModel).filter(ErpModel.id == erp_id)
        result = await session.execute(query)
        erp: ErpSchemaBase = result.scalars().unique().one_or_none()

        if erp:
            return erp
        else:
            raise HTTPException(detail="ERP não encontrado", status_code=status.HTTP_404_NOT_FOUND)


@router.put("/{erp_id}", response_model=ErpSchemaBase, status_code=status.HTTP_202_ACCEPTED)
async def put_erp(
    erp_id: int,
    erp: ErpSchemaBase,
    db: AsyncSession = Depends(get_session),
    usuario_logado: UsuarioModel = Depends(get_current_user),
):

    if not usuario_logado.eh_admin:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Não autorizado")

    async with db as session:
        query = select(ErpModel).filter(ErpModel.id == erp_id)
        result = await session.execute(query)
        erp_update: ErpSchemaBase = result.scalars().unique().one_or_none()

        if erp_update:
            if erp.ip:
                erp_update.ip = erp.ip
            if erp.login:
                erp_update.login = erp.login
            if erp.senha:
                erp_update.senha = erp.senha
            if erp.identificador:
                erp_update.identificador = erp.identificador
            if erp.vendor:
                erp_update.vendor = erp.vendor

            await session.commit()
            return erp_update

        else:
            raise HTTPException(detail="ERP não encontrado", status_code=status.HTTP_404_NOT_FOUND)


@router.delete("/{erp_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_erp(
    erp_id: int, db: AsyncSession = Depends(get_session), usuario_logado: UsuarioModel = Depends(get_current_user)
):

    if not usuario_logado.eh_admin:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Não autorizado")

    async with db as session:
        query = select(ErpModel).filter(ErpModel.id == erp_id)
        result = await session.execute(query)
        erp_del: ErpSchemaBase = result.scalars().unique().one_or_none()

        if erp_del:
            await session.delete(erp_del)
            await session.commit()
            return Response(status_code=status.HTTP_204_NO_CONTENT)

        else:
            raise HTTPException(detail="ERP não encontrado", status_code=status.HTTP_404_NOT_FOUND)
