import connexion
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
# Crie a aplicação connexion
app = connexion.App(__name__, specification_dir=".")

# Leia a especificação OpenAPI e crie os endpoints
app.add_api("api_definition.yaml")

if __name__ == "__main__":
    app.run(debug=True)


# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
# initialize the app with the extension
db.init_app(app)
