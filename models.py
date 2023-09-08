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
    
class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    preco = db.Column(db.Float)
    saldo = db.Column(db.Integer)
    produtos = db.relationship('ItensVenda', backref='produtos')

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
    quantidade = db.Column(db.Integer, nullable=False)
    
# Schemas from Jason >.>
class ClienteSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Cliente
    
    id = ma.auto_field()
    nome = ma.auto_field()
    email = ma.auto_field()
    celular = ma.auto_field()
    senha = ma.auto_field()

class ProdutoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Produto

    id = ma.auto_field()
    nome = ma.auto_field()
    preco = ma.auto_field()
    saldo = ma.auto_field()

class CompradorSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Comprador

    id = ma.auto_field()
    nome = ma.auto_field()
    cpf = ma.auto_field()

class VendaSchema(ma.SQLAlchemyAutoSchema):
    comprador = ma.Nested(CompradorSchema)
    class Meta:
        model = Venda
    
    id = ma.auto_field()
    compradorId = ma.auto_field()

class ItensVendaSchema(ma.SQLAlchemyAutoSchema):
    produtos = ma.Nested(ProdutoSchema)
    vendas = ma.Nested(VendaSchema)
    class Meta:
        model = ItensVenda

    id = ma.auto_field()
    produto_id = ma.auto_field()
    venda_id = ma.auto_field()
    quantidade = ma.auto_field()


    
    
