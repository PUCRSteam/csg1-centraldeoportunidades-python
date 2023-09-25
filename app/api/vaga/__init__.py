from flask import Flask, Blueprint
from flask_restx import Api

def get_api(app: Flask, path: str):

	blueprint = Blueprint('bp_api_vaga', __name__)
	vaga_api = Api(blueprint, title='Vaga REST API')

	from .controller import ns
	vaga_api.add_namespace(ns, '/vagas')

	app.register_blueprint(blueprint, url_prefix=path)
    