from flask import Flask

def start_apis(app: Flask, url: str):
    from .vaga import get_api as get_vaga_api

    get_vaga_api(app, f'{url}')
