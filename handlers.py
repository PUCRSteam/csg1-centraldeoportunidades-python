def criar_vaga():
    # Sua lógica aqui
    print("Criando vaga")
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
