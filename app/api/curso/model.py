from pydantic import BaseModel
from typing import List

class Curso(BaseModel):
    __tablename__ = 'cursos'

    id: int

    curso: str
    