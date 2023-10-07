from os import getenv
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Api configs.
    API_TITLE: str = "CENTRAL_DE_OPORTUNIDADES"
    API_HOST: str = "0.0.0.0"
    API_PORT: int = 443

    # SSL configs.
    # If running locally, point to your certificate and private key files.
    SSL_CERT_FILE: str = "/etc/ssl/certificate.crt"
    SSL_KEY_FILE: str = "/etc/ssl/private.key"

    # DB configs.
    # If using Docker, define the environment variable in Dockerfile / docker-compose.yml
    DB_HOST: str = getenv("MONGODB_HOST", "mongodb://localhost:27017")
    DB_NAME: str = "central-de-oportunidades"
    #
    # DB ENV for runing tests.
    # Set the 'DB_ENVIRONMENT' environment variable to 'test' when running tests.
    DB_ENVIRONMENT: str = "test"


settings = Settings()
