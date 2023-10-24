from pymongo.database import Database
from pymongo.results import UpdateResult, DeleteResult, InsertOneResult
from app.api.curso.model import Curso

CURSO_COLLECTION = "cursos"


class CursoRepository:
    def __init__(self, database: Database):
        self._collection = database[CURSO_COLLECTION]

    def find_by_id(self, id: int) -> Curso:
        curso_dict = self._collection.find_one({"id": id})
        return Curso.parse_obj(curso_dict)
