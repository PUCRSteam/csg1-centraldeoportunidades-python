from flask import Flask
from dotenv import load_dotenv

load_dotenv()

from config import start_config
from extensions import start_extensions


def create_app() -> Flask:
    app = Flask(__name__)
    
    start_config(app)

    start_extensions(app)

    with app.app_context():
        from api import start_apis
        start_apis(app, '/api')


    return app



if __name__ == "__main__":
    app = create_app()    

    app.run()
    