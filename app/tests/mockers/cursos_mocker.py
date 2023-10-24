from app.api.curso.model import Curso

def mock_curso_with_default_params():
    return Curso(
        id=1,
        nome="Ciência da Computação",
        isDeleted=False
    )