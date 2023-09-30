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

def get_vaga_router() -> APIRouter:
    return _vaga_router