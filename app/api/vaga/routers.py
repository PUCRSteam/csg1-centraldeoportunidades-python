from typing import List
from app.api.vaga.model import Vaga
from fastapi import APIRouter
from app.api.vaga.repository import VagaRepository
from app.api.vaga.services import VagaService
from app.extensions.database import get_database

_database = get_database()
_vaga_repository = VagaRepository(_database)
_vaga_service = VagaService(_vaga_repository)
_vaga_router = APIRouter(prefix="/vagas")


@_vaga_router.post("/create")
def create_vaga(vaga_data: Vaga) -> Vaga:
    return _vaga_service.create(vaga_data)


@_vaga_router.get("/id={id_vaga}")
def get_vaga_by_id(id_vaga: int) -> Vaga:
    return _vaga_service.get_by_id(id_vaga)


@_vaga_router.get("/idAnunciante={id_anunciante}")
def get_vagas_by_id_anunciante(id_anunciante: int) -> List[Vaga]:
    return _vaga_service.get_by_id_anunciante(id_anunciante)


def get_vaga_router() -> APIRouter:
    return _vaga_router


@_vaga_router.get("/id_curso={id_curso}")
def get_vagas_from_curso(id_curso: int) -> List[Vaga]:
    return _vaga_service.get_vagas_from_curso(id_curso)


@_vaga_router.get("/id_vaga={id_vaga}")
def delete_vaga(id_vaga: int):
    return _vaga_service.delete_vaga(id_vaga)


@_vaga_router.get("/id_vaga={id_vaga}")
def edit_vaga(id_vaga: int, vaga_data: Vaga) -> Vaga:
    return _vaga_service.edit_vaga(id_vaga, vaga_data)
