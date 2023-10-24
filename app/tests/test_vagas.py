import pytest
from fastapi.testclient import TestClient
from fastapi import status

from app.tests.mockers.vaga_mocker import mock_vaga_with_default_params


# This fixture will be executed before each test.
# It will create a TestClient instance and pass it to the test function.
# The test function will be able to send requests to the application.
@pytest.fixture(scope="module")
def test_app():
    yield TestClient(app=app)



# test get vaga id 1
def get_vaga(test_app: TestClient):
    response = test_app.get("/vagas/1")
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "idAnunciante": 1,
        "descricao": "Vaga de Estágio em Desenvolvimento de Software",
        "cargaHoraria": 6,
        "auxilioTransporte": True,
        "auxilioAlimentacao": True,
        "quantidadeVagas": 1,
        "cursos": [1, 2, 3],
        "isDeleted": False
    }
