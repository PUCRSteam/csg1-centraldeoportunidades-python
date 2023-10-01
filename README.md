# csg1-centraldeoportunidades-python

## How to run

- Instalar gerenciador de dependências abaixo:
    ```bash
    pip install "poetry==1.4.1"
    ```

- Instalar dependências do projeto:
    ```bash
    poetry install
    ```
- Run: 
    ```bash
    poetry run uvicorn app.main:app --reload or poetry shell -> uvicorn app.main:app --reload
    ```