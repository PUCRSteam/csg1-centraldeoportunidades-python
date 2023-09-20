from flask import request
from database.adapter import getDatabase

db = getDatabase()

def criar_vaga():
    #insert into vagas
    dados = request.get_json()
    db.session.add(dados)
    db.session.commit()
    #colocar em try catch pipipi popopo erro de commit etc
    return "Vaga criada", 201


def getVagaPorId(id):
    # Sua lógica aqui
    print("Vaga", id)
    return "Vaga", 200


def getVagaPorAnunciante(idAnunciante):
    # Sua lógica aqui
    print("Vagas", idAnunciante)
    return "Vagas", 200


def getVagasAlunoCurso(idCandidato, idCurso):
    # Sua lógica aqui
    print("Vagas", idCandidato, idCurso)
    return "Vagas", 200


def editar_vaga(id):
    # Sua lógica aqui
    print("Editar vaga", id)
    return "Editar vaga", 200


def criar_alerta(id):
    # Sua lógica aqui
    print("Criar alerta", id)
    return "Criar alerta", 200


def getAlertasCandidato(idCandidato):
    # Sua lógica aqui
    print("Alertas", idCandidato)
    return "Alertas", 200
