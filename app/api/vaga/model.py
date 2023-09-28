from app.extensions.database import db

class Vaga(db.Model):
    __tablename__ = 'vagas'

    __table_args__ = (db.UniqueConstraint('idAnunciante', 'id'))

    id: int = db.Column(db.Integer, primary_key=True)

    idAnunciante: int = db.Column(db.Integer, nullable=False)

    descricao: str = db.Column(db.String, nullable=False)

    cargaHoraria: int = db.Column(db.Integer, nullable=False)

    auxilioTransporte: bool = db.Column(db.Boolean, nullable=False)

    auxilioAlimentacao: bool = db.Column(db.Boolean, nullable=False)

    quantidadeVagas: int = db.Column(db.Integer, nullable=False)

    cursos: list = db.relationship('Curso', backref='vagas', lazy=True)

    isDeleted: bool = db.Column(db.Integer, nullable=True, default=False)
