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
    preco = db.Column(db.Float)
    saldo = db.Column(db.Integer)

class Comprador(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    cpf = db.Column(db.String(11))
    comprador = db.relationship('Venda', backref='comprador')

class Venda(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    compradorId = db.Column(db.Integer, db.ForeignKey('comprador.id'), nullable=False)
    produtos = db.relationship('Produto', secondary='itensvenda', backref='vendas', lazy='joined')

itensvenda = db.Table('itensvenda', db.Column('produto_id',db.Integer, db.ForeignKey('produto.id')), db.Column('venda_id',db.Integer, db.ForeignKey('venda.id')))

'''class ItensVenda(db.Model):
    produtoId = db.Column(db.Integer, db.ForeignKey('produto.id'), nullable=False,primary_key=True)
    vendaId= db.Column(db.Integer, db.ForeignKey('venda.id'), nullable=False,primary_key=True)'''

# Schemas from Jason >.>
class ClienteSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Cliente
    
    id = ma.auto_field()
    nome = ma.auto_field()
    email = ma.auto_field()
    celular = ma.auto_field()
    senha = ma.auto_field()
    confsenha = ma.auto_field()

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
    produtos = ma.Nested(ProdutoSchema, many=True)
    class Meta:
        model = Venda
    
    id = ma.auto_field()
    compradorId = ma.auto_field()


    
    
