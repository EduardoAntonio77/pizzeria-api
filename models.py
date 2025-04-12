from datetime import datetime, timezone
from database import db

class Negocio(db.Model):
    __tablename__ = 'pizzerias'
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String(100), nullable = False)
    owner_name = db.Column(db.String(100), nullable = False)
    address = db.Column(db.String(200), nullable = False)
    created_at = db.Column(db.DateTime, default = datetime.now(timezone.utc))
    deleted_at = db.Column(db.DateTime, nullable = True)

    tabela_pizzas = db.relationship('Produto', backref = 'pizzerias', lazy = True)


class Produto(db.Model):
    __tablename__ = 'pizzas'
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    flavor = db.Column(db.String(100), nullable = False)
    pizza_type = db.Column(db.String(100), nullable = False)
    price = db.Column(db.Integer, nullable = False)
    created_at = db.Column(db.DateTime, default = datetime.now(timezone.utc))
    deleted_at = db.Column(db.DateTime, nullable = True)


    pizzerias_id = db.Column(db.Integer, db.ForeignKey('pizzerias.id'), nullable = False)
