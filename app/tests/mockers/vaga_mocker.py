from app.api.vaga.model import Vaga

def mock_vaga_with_default_params():
    return Vaga(
        id=1,
        idAnunciante=1,
        descricao="Vaga de Estágio em Desenvolvimento de Software",
        cargaHoraria=6,
        auxilioTransporte=True,
        auxilioAlimentacao=True,
        quantidadeVagas=1,
        cursos=[1, 2, 3],
        isDeleted=False
    )
    
