from pymongo.database import Database
from pymongo.results import UpdateResult, DeleteResult, InsertOneResult
from app.api.vaga.model import Vaga

VAGA_COLLECTION = "vagas"


class VagaRepository:
    def __init__(self, database: Database):
        self._collection = database[VAGA_COLLECTION]

    def create(self, vaga_data: Vaga) -> InsertOneResult:
        # On create we need to convert vaga_data to dict and then insert it into the database.
        return self._collection.insert_one(vaga_data.dict())

    def find_by_id(self, vaga_id: int):
        vaga_dict = self._collection.find_one({"id": vaga_id})
        return Vaga.parse_obj(vaga_dict)
        