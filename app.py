from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
  return "Hellowfwefwe World!"

@app.route("/criar-vaga")
def criar_vaga():
  return "Cria uma vfwfwfwfa"

if __name__ == "__main__":
  app.run()
