# Modelo
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
db = SQLAlchemy()
ma = Marshmallow()

class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    email = db.Column(db.String(100))
    celular = db.Column(db.String(100))
    senha = db.Column(db.String(30))
    confsenha = db.Column(db.String(30))

# D
class ClienteSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nome', 'email', 'celular', 'senha', 'confsenha')
