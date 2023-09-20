from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

def getDatabase():
    global db
    return db

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
# Crie a aplicação connexion

def initDb(app):
    app.app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
    db.init_app(app.app)
    
    with app.app.app_context():
        db.create_all()