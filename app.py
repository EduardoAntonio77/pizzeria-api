# Imports.
from flask import Flask, request, jsonify
from database import db
from models import Negocio, Produto
import datetime
from flask_migrate import Migrate
from flask_cors import CORS

# Essential app config.
app = Flask(__name__)
CORS(app, origins="http://localhost:3000")
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost:3306/pizzeriaapi' # Esta conectando a database criada ao app
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # Pesquisar sobre

db.init_app(app) # Foi criada uma sessão e a database foi iniciada em app
migrate = Migrate(app, db) # Ao executar o comando flask db migrate no terminal, estara migrando os models de app para o banco de dados.

# Slash route.
@app.route("/")
def slash_route():
    return jsonify({
        "status": 200,
        "message": "Pizzeria API.",
        "version": '0.1'
    }), 200

# Create pizza route
@app.route("/pizza", methods=['POST'])
def create_pizza():
    data = request.json
    new = Produto(
        flavor=data["flavor"],
        pizza_type=data["pizza_type"],
        price=data["price"],
        pizzerias_id=data["pizzerias_id"]
    ) # Criou um novo produto baseado no model "Produto" preenchendo as colunas que não se auto completam

    db.session.add(new) # lembrando que a sessão foi iniciada na linha 15, aqui estamos adicionando o novo produto a sessão atual (database local)

    db.session.commit() # enviando as alterações feitas para o banco de dados mysql (remoto).(grande semelhança com git add e git commit)

    return jsonify({
        "status": 200,
        "message": "Pizza criada!",
        "id": new.id # Este id existe no model Produto porem, ele se cria sozinho
    })

# App init.
if __name__ == "__main__":
    app.run(debug=True)


