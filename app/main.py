import uvicorn
from app.api.vaga.routers import get_vaga_router
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from firebase_admin import credentials, firestore, initialize_app
from app.config import settings


def init_app() -> FastAPI:
    app = FastAPI(title=settings.API_TITLE)

    #include routers
    app.include_router(get_vaga_router())

    #CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["OPTIONS", "GET", "POST", "PUT", "DELETE", "PATCH"],
        allow_headers=["*"]
    )
    return app


app = init_app()

if __name__ == '__main__':
    uvicorn.run(app,
                reload=True,
                host=settings.API_HOST,
                port=settings.API_PORT,
                #ssl_certfile=settings.SSL_CERT_FILE,
                #ssl_keyfile=settings.SSL_KEY_FILE
    )
