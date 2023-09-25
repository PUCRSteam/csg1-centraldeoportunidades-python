from app.extensions.database import db

class Vaga(db.Model):
    __tablename__ = 'cursos'

    id: int = db.Column(db.Integer, primary_key=True)

    curso: str = db.Column(db.String, nullable=False)
