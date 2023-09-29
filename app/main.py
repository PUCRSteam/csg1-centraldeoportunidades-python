import os
from flask import Flask, request, jsonify
from firebase_admin import credentials, firestore, initialize_app
from app.extensions import start_extensions


def create_app():
    app = Flask(__name__)
    start_extensions(app)
    @app.route("/")
    def hello():        
        return "hello"
    return app


port = int(os.environ.get('PORT', 8080))

if __name__ == '__main__':
    app = create_app()
    
    app.run(host='0.0.0.0', port=port, debug=True)