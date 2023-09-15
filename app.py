import connexion

# Crie a aplicação connexion
app = connexion.App(__name__, specification_dir='.')

# Leia a especificação OpenAPI e crie os endpoints
app.add_api('api_definition.yaml')

if __name__ == '__main__':
    app.run(debug=True)
