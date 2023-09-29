from flask import Flask

from app.extensions.database import _initialize_db


def start_extensions(app: Flask):
	
	_initialize_db()

