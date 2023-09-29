from .model import Vaga
from ...extensions.database import db
from typing import List

#vagas_ref = db.collection('vagas')

#classe repository interage com fb
class VagaRepository:
    def create_vaga(vaga: Vaga) -> Vaga:    
        #tbd
        return

    def get_vaga_id(id: int) -> Vaga:
        return #tbd

    def get_vagas_anunciante(idAnunciante: int) -> List[Vaga]:
        return #tbd

    def get_vagas_aluno_curso(idCurso: int) -> List[Vaga]:
        return #tbd
