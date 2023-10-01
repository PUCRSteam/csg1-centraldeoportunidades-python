from fastapi import HTTPException
from typing import List
from app.api.vaga.model import Vaga
from app.api.vaga.repository import VagaRepository

class VagaService:
    def __init__(self, repository: VagaRepository):
        self._repository = repository

    def create(self, vaga_data: Vaga) -> Vaga:
        try:            
            result = self._repository.create(vaga_data)
            return self._repository.find_by_id(result.inserted_id)
        except ValueError as e:
            raise HTTPException(
                status_code=400, detail=e.args[0])

    def get_by_id(self, id_vaga: int) -> Vaga:
        try:
            return self._repository.find_by_id(id_vaga)
        except Exception:
            raise HTTPException(
                status_code=404, detail="Vaga não encontrada."
            )

    def get_by_id_anunciante(self, id_anunciante: int) -> List[Vaga]:
        try:
            return self._repository.get_by_id_anunciante(id_anunciante)
        except Exception:
            raise HTTPException(
                status_code=404, detail="Vagas não encontradas."
            )