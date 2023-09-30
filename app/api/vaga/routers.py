from typing import List
from app.api.vaga.model import Vaga
from fastapi import APIRouter, File, Form, UploadFile
from app.api.vaga.repository import VagaRepository
from app.api.vaga.services import VagaService
from app.extensions.database import get_database

_database = get_database()
_vaga_repository = VagaRepository(_database)
_vaga_service = VagaService(_vaga_repository)
_vaga_router = APIRouter(prefix="/vagas")


@_vaga_router.post("/create")
def create_pdf(vaga_data: Vaga) -> Vaga:
    return _vaga_service.create(vaga_data)

def get_vaga_router() -> APIRouter:
    return _vaga_router