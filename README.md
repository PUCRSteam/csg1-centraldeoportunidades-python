# csg1-centraldeoportunidades-python

Serviço de Central de Oportunidades: Essencial para o engajamento dos alunos e sua interação com empresas parceiras e oportunidades de carreira, é um componente-chave do domínio do negócio.

## Pré-requisitos
- [Python](https://python.org/) `^3.10` <br/>
- [Poetry](https://python-poetry.org/docs/)

## How to run

- Instalar gerenciador de dependências abaixo:
- 
    - Linux, macOS, Windows (WSL)
      
    ```bash
    curl -sSL https://install.python-poetry.org | python3 -
    ```
    
    - Windows (Powershell)
      
    ```bash
    (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
    ```

    

- Instalar dependências do projeto (certifiqe-se de estar com a versão do Python ^1.10.0):
    ```bash
    poetry install
    ```
- Run: 
    ```bash
    poetry run uvicorn app.main:app --reload
    ```
    or
    ```bash
    poetry shell
    uvicorn app.main:app --reload
    ```
