# Resources
from flask_restful import Resource, reqparse, abort
from flask import jsonify
from models import db,Cliente,ClienteSchema,Produto,ProdutoSchema, Comprador, CompradorSchema, Venda,VendaSchema

class ClienteResource(Resource):
    def get(self, cliente_id=None):
        if cliente_id is None:
            cliente = Cliente.query.all()
            return ClienteSchema(many=True).dumps(cliente)
        
        cliente = Cliente.query.get(cliente_id)
        return ClienteSchema().dumps(cliente)
    
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('nome', type=str, required=True)
        parser.add_argument('email', type=str, required=True)
        parser.add_argument('celular', type=str, required=True)
        parser.add_argument('senha', type=str, required=True)
        parser.add_argument('confsenha', type=str, required=True)
        args = parser.parse_args()

        cliente = Cliente(nome=args['nome'], 
                          email=args['email'],
                          celular=args['celular'],
                          senha=args['senha'],
                          confsenha=args['confsenha']
                          )

        db.session.add(cliente)
        db.session.commit()
        return ClienteSchema().dump(cliente)
    
    def delete(self, cliente_id=None):
        if cliente_id is None:
            abort(404, message="ID {} do Cliente não encontrado".format(cliente_id))
        Cliente.query.filter_by(id=cliente_id).delete()
        db.session.commit()

        return jsonify(msg = {
            "Resposta": "Cliente {} Deletado com Sucesso".format(cliente_id)
        })
    
    def put(self, cliente_id=None):
        if cliente_id is None:
            abort(404, message="ID {} do tutor não encontrado".format(cliente_id))

        parser = reqparse.RequestParser()
        parser.add_argument('nome', type=str, required=True)
        parser.add_argument('email', type=str, required=True)
        parser.add_argument('celular', type=str, required=True)
        parser.add_argument('senha', type=str, required=True)
        parser.add_argument('confsenha', type=str, required=True)
        args = parser.parse_args()
        
        cliente = Cliente.query.get(cliente_id)

        cliente.nome = args['nome']
        cliente.email = args['email']
        cliente.celular = args['celular']
        cliente.senha = args['senha']
        cliente.confsenha = args['confsenha']

        db.session.commit()
        return ClienteSchema().dump(cliente)

class ProdutoResource(Resource):
    def get(self, produto_id = None):
        if produto_id is None:
            produtos = Produto.query.all()
            return ProdutoSchema(many=True).dumps(produtos)
        produto = Produto.query.get(produto_id)
        return ProdutoSchema().dumps(produto)

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('nome', type=str, required=True)
        parser.add_argument('preco', type=float, required=True)
        parser.add_argument('saldo', type=int, required=False)
        args = parser.parse_args()

        produto = Produto(nome=args['nome'],
                          preco=args['preco'],
                          saldo=args['saldo'])
    
    def delete(self, produto_id = None):
        if produto_id is None:
            abort(404, message="ID {} do Cliente não encontrado".format(produto_id))
        Produto.query.filter_by(id=produto_id).delete()
        db.session.commit()

        return jsonify(msg = {
            "Resposta": "Produto {} Deletado com Sucesso".format(produto_id)
        })

    def put(self, produto_id=None):
        if produto_id is None:
            abort(404, message="ID {} do Produto não encontrado".format(produto_id))
        
        parser = reqparse.RequestParser()
        parser.add_argument('nome', type=str, required=True)
        parser.add_argument('preco', type=float, required=True)
        parser.add_argument('saldo', type=int, required=False)
        args = parser.parse_args()

        produto = Produto.query.get(produto_id)

        produto.nome = args['nome']
        produto.preco = args['preco']
        produto.saldo = args['saldo']

        db.session.commit()
        return ProdutoSchema().dumps(produto)

class CompradorResource(Resource):
    def get(self, comprador_id = None):
        if comprador_id is None:
            comprador = Comprador.querry.all
            return CompradorSchema(many=True).dumps(comprador)

        comprador = Comprador.query.get(comprador_id)
        return CompradorSchema().dumps(comprador)

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('nome', type=str, required=True)
        parser.add_argument('cpf', type=str, required=True)
        args = parser.parse_args()

        comprador = Comprador(nome=args['nome'],
        cpf=args['cpf']
        )
        db.session.add(comprador)
        db.session.commit()
        
        return CompradorSchema().dumps(comprador)

    def delete(self, comprador_id = None):
        if comprador_id is None:
            abort(404, message="ID {} do Comprador não encontrado".format(comprador_id))
        Produto.query.filter_by(id=comprador_id).delete()
        db.session.commit()

        return jsonify(msg = {
            "Resposta": "Cliente {} Deletado com Sucesso".format(comprador_id)
        })

    def put(self, comprador_id = None):
        if comprador_id is None:
            abort(404, message="ID {} do Comprador não encontrado".format(comprador_id))

        parser = reqparse.RequestParser()
        parser.add_argument('nome', type=str, required=True)
        parser.add_argument('cpf', type=str, required=True)
        args = parser.parse_args()
        
        comprador = Comprador.query.get(comprador_id)

        comprador.nome = args['nome']
        comprador.email = args['cpf']

        db.session.commit()
        return ClienteSchema().dump(comprador)

class VendaResource(Resource):
    def get(self, venda_id = None):
        if venda_id is None:
            vendas = Venda.querry.all()
            return VendaSchema().dumps(vendas)

        venda = Venda.query.get(venda_id)
        return VendaSchema().dumps(venda)

    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument('compradorId', type=str, required=True)
        args = parser.parse_args()

        Venda = Cliente(nome=args['compradorId'])

        db.session.add(Venda)
        db.session.commit()
        return ClienteSchema().dump(Venda)