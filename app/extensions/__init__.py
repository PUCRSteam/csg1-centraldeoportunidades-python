from flask import Flask
from flask_sqlalchemy.query import Query
from flask import Flask

from extensions.database import db
from extensions.migration import migrate
from extensions.cors import cors


def start_extensions(app: Flask):
	
	db.init_app(app)
	migrate.init_app(app, db)
	cors.init_app(app)

