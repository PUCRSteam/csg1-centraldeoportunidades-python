import connexion

from database.adapter import initDb


app = connexion.App(__name__, specification_dir=".")

# Leia a especificação OpenAPI e crie os endpoints
app.add_api("api_definition.yaml")



if __name__ == "__main__":
    initDb(app)    
    app.run(debug=True)