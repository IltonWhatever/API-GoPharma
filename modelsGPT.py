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
    preco = db.Column(db.Float)
    saldo = db.Column(db.Integer)
    vendas = db.relationship('Venda', secondary='itensvenda', backref='produtos')

class Comprador(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    cpf = db.Column(db.String(11))
    vendas = db.relationship('Venda', backref='comprador')

class Venda(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    compradorId = db.Column(db.Integer, db.ForeignKey('comprador.id'), nullable=False)

class ItensVenda(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    produto_id = db.Column(db.Integer, db.ForeignKey('produto.id'), nullable=False)
    venda_id = db.Column(db.Integer, db.ForeignKey('venda.id'), nullable=False)

class ClienteSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Cliente

class ProdutoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Produto

class CompradorSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Comprador

class VendaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Venda

class ItensVendaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ItensVenda
