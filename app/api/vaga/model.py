from pydantic import BaseModel
from typing import List

class Vaga(BaseModel):
    id: int

    idAnunciante: int

    descricao: str

    cargaHoraria: int

    auxilioTransporte: bool

    auxilioAlimentacao: bool

    quantidadeVagas: int

    cursos: List[Curso] = []

    isDeleted: bool
    