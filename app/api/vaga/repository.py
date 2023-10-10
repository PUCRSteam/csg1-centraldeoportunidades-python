from pymongo.database import Database
from pymongo.results import UpdateResult, DeleteResult, InsertOneResult
from app.api.vaga.model import Vaga

VAGA_COLLECTION = "vagas"


class VagaRepository:
    def __init__(self, database: Database):
        self._collection = database[VAGA_COLLECTION]

    def create(self, vaga_data: Vaga) -> InsertOneResult:
        return self._collection.insert_one(vaga_data.dict())

    def find_by_id(self, vaga_id: int) -> Vaga:
        vaga_dict = self._collection.find_one({"id": vaga_id})
        return Vaga.parse_obj(vaga_dict)

    def get_by_id_anunciante(self, id_anunciante: int) -> list[Vaga]:
        vagas_anunciante = []
        vagas_dict = list(self._collection.find({"idAnunciante": id_anunciante}))
        for vaga in vagas_dict:
            vagas_anunciante.append(vaga.parse_obj(Vaga))
        return vagas_anunciante

    def get_vagas_from_curso(self, id_curso: int) -> list[Vaga]:
        list_vagas = []
        vagas_dict = list(
            self._collection.find({"document_up.cursos": {"$in": ["{id_curso}"]}})
        )
        # vagas_dict = list(self._collection.find({"cursos": filtro}))
        for vaga in vagas_dict:
            list_vagas.append(vaga.parse_obj(Vaga))
        return list_vagas

    def delete_vaga(self, id_vaga: int) -> DeleteResult:
        delete_query = self._collection.find({"id": id_vaga})
        return self._collection.delete_one(delete_query)

    def edit_vaga(self, id_vaga: int, vaga_data: Vaga) -> UpdateResult:
        update_query = self._collection.find({"id": id_vaga})
        return self._collection.update_one(update_query, vaga_data)
