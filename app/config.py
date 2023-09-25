import os, random, string
from flask import Flask

def get_env(name, required=True):
    try:
        return os.environ[name]
    except KeyError:
        if required:
            error = "Environment variable '{}' not found.".format(name)
            raise Exception(error)

class Config(object):
    DB_ENGINE = get_env('DB_ENGINE')
    DB_HOST = get_env('DB_HOST')
    DB_USERNAME = get_env('DB_USERNAME')
    DB_PASSWORD = get_env('DB_PASSWORD')
    DB_PORT = get_env('DB_PORT')
    DB_NAME = get_env('DB_NAME')

    SQLALCHEMY_DATABASE_URI = f'{DB_ENGINE}://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    KEY = 'key1!'

    AUTH_SERVICE_API_URL = get_env('AUTH_SERVICE_API_URL', required=False)

class Development(Config):
    FLASK_DEBUG = 1

def start_config(app: Flask):
    config = Development()
    app.config.from_object(config)