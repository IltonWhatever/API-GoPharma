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
    
class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    preco = db.Column(db.Double)
    saldo = db.Column(db.Integer)
    vendas = db.relationship('Venda', secondary='ItensVenda', backref='produtos')

class Comprador(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    cpf = db.Column(db.String(11))

class Venda(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    compradorId = db.Column(db.Integer, db.ForeignKey('comprador.id'), nullable=False)
    comprador = db.relationship('Comprador')
    produtos = db.relationship('Produto', secondary='ItensVenda', backref='vendas')

class ItensVenda(db.Model):
    produtoId = db.Column(db.Integer, db.ForeignKey('produto.id'), nullable=False,primary_key=True)
    vendaId= db.Column(db.Integer, db.ForeignKey('venda.id'), nullable=False,primary_key=True)

# D
class ClienteSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nome', 'email', 'celular', 'senha', 'confsenha')
