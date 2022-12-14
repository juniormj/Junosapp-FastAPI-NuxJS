from typing import List

from database.auth import autenticacar, criar_token_acesso
from database.deps import get_current_user, get_session
from database.security import gerar_hash_senha
from fastapi import APIRouter, Depends, HTTPException, Response, status
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm
from models.usuario_model import UsuarioModel
from schemas.usuario_schema import UsuarioSchemaBase, UsuarioSchemaCreate, UsuarioSchemaUp
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

router = APIRouter()


@router.get("/logado", response_model=UsuarioSchemaBase)
def get_logado(usuario_logado: UsuarioModel = Depends(get_current_user)):
    return usuario_logado


@router.post("/signup", status_code=status.HTTP_201_CREATED, response_model=UsuarioSchemaBase)
async def post_usuario(
    usuario: UsuarioSchemaCreate,
    db: AsyncSession = Depends(get_session),
    usuario_logado: UsuarioModel = Depends(get_current_user),
):

    if not usuario_logado.eh_admin:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Não autorizado")

    if usuario.senha == "" or usuario.senha is None:
        raise HTTPException(status_code=status.HTTP_405_METHOD_NOT_ALLOWED, detail="O campo Senha não pode está vazio")

    novo_usuario: UsuarioModel = UsuarioModel(
        nome=usuario.nome,
        sobrenome=usuario.sobrenome,
        email=usuario.email,
        senha=gerar_hash_senha(usuario.senha),
        eh_admin=usuario.eh_admin,
    )

    async with db as session:
        try:
            session.add(novo_usuario)
            await session.commit()
            return novo_usuario
        except IntegrityError:
            raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="Esse E-mail já está cadastrado")


@router.post("/login")
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: AsyncSession = Depends(get_session),
):
    usuario = await autenticacar(email=form_data.username, senha=form_data.password, db=db)

    if not usuario:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Dados de acesso incorreto")

    return JSONResponse(
        content={
            "access_token": criar_token_acesso(sub=usuario.id),
            "token_type": "bearer",
        },
        status_code=status.HTTP_200_OK,
    )


@router.get("/", response_model=List[UsuarioSchemaBase])
async def get_usuarios(
    db: AsyncSession = Depends(get_session),
    usuario_logado: UsuarioModel = Depends(get_current_user),
):
    if not usuario_logado.eh_admin:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Não autorizado")

    async with db as session:
        query = select(UsuarioModel)
        result = await session.execute(query)
        usuarios: List[UsuarioSchemaBase] = result.scalars().unique().all()

        return usuarios


@router.get("/{usuario_id}", response_model=UsuarioSchemaBase)
async def get_usuario(
    usuario_id: int,
    db: AsyncSession = Depends(get_session),
    usuario_logado: UsuarioModel = Depends(get_current_user),
):
    if not usuario_logado.eh_admin:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Não autorizado")

    async with db as session:
        query = select(UsuarioModel).filter(UsuarioModel.id == usuario_id)
        result = await session.execute(query)
        usuario: UsuarioSchemaBase = result.scalars().unique().one_or_none()

        if usuario:
            return usuario
        else:
            raise HTTPException(detail="Usuário não encontrado", status_code=status.HTTP_404_NOT_FOUND)


@router.put(
    "/{usuario_id}",
    response_model=UsuarioSchemaBase,
    status_code=status.HTTP_202_ACCEPTED,
)
async def put_usuario(
    usuario_id: int,
    usuario: UsuarioSchemaUp,
    db: AsyncSession = Depends(get_session),
    usuario_logado: UsuarioModel = Depends(get_current_user),
):
    if not usuario_logado.eh_admin:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Não autorizado")

    async with db as session:
        query = select(UsuarioModel).filter(UsuarioModel.id == usuario_id)
        result = await session.execute(query)
        usuario_update: UsuarioSchemaBase = result.scalars().unique().one_or_none()

        if usuario_update:
            if usuario.nome:
                usuario_update.nome = usuario.nome
            if usuario.sobrenome:
                usuario_update.sobrenome = usuario.sobrenome
            if usuario.email:
                usuario_update.email = usuario.email
            if usuario.eh_admin != usuario_update.eh_admin:
                usuario_update.eh_admin = usuario.eh_admin
            if usuario.senha:
                usuario_update.senha = gerar_hash_senha(usuario.senha)

            await session.commit()
            return usuario_update

        else:
            raise HTTPException(detail="Usuário não encontrado", status_code=status.HTTP_404_NOT_FOUND)


@router.delete("/{usuario_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_usuario(
    usuario_id: int,
    db: AsyncSession = Depends(get_session),
    usuario_logado: UsuarioModel = Depends(get_current_user),
):
    if not usuario_logado.eh_admin:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Não autorizado")

    async with db as session:
        query = select(UsuarioModel).filter(UsuarioModel.id == usuario_id)
        result = await session.execute(query)
        usuario_del: UsuarioSchemaBase = result.scalars().unique().one_or_none()

        if usuario_del:
            await session.delete(usuario_del)
            await session.commit()
            return Response(status_code=status.HTTP_204_NO_CONTENT)
        else:
            raise HTTPException(detail="Usuário não encontrado", status_code=status.HTTP_404_NOT_FOUND)
