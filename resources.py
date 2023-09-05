# Resources
from flask_restful import Resource, reqparse, abort
from flask import jsonify
from models import db,Cliente,ClienteSchema,Produto,ProdutoSchema, Comprador, CompradorSchema, Venda,VendaSchema, ItensVenda, ItensVendaSchema

class ClienteResource(Resource):
    def get(self, cliente_id=None):
        if cliente_id is None:
            cliente = Cliente.query.all()
            return ClienteSchema(many=True).dump(cliente)
        
        cliente = Cliente.query.get(cliente_id)
        return ClienteSchema().dump(cliente)
    
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('nome', type=str, required=True)
        parser.add_argument('email', type=str, required=True)
        parser.add_argument('celular', type=str, required=True)
        parser.add_argument('senha', type=str, required=True)
        args = parser.parse_args()

        cliente = Cliente(nome=args['nome'], 
                          email=args['email'],
                          celular=args['celular'],
                          senha=args['senha']
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
        args = parser.parse_args()
        
        cliente = Cliente.query.get(cliente_id)

        cliente.nome = args['nome']
        cliente.email = args['email']
        cliente.celular = args['celular']
        cliente.senha = args['senha']

        db.session.commit()
        return ClienteSchema().dump(cliente)

class ProdutoResource(Resource):
    def get(self, produto_id = None):
        if produto_id is None:
            produtos = Produto.query.all()
            return ProdutoSchema(many=True).dump(produtos)
        produto = Produto.query.get(produto_id)
        return ProdutoSchema().dump(produto)

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('nome', type=str, required=True)
        parser.add_argument('preco', type=float, required=True)
        parser.add_argument('saldo', type=int, required=False)
        args = parser.parse_args()

        if args['saldo'] is None:
            args['saldo'] = 0 

        produto = Produto(nome=args['nome'],
                          preco=args['preco'],
                          saldo=args['saldo'])
        
        db.session.add(produto)
        db.session.commit()

        return ProdutoSchema().dump(produto)
    
    def delete(self, produto_id = None):
        if produto_id is None:
            abort(404, message="ID {} do Produto não encontrado".format(produto_id))
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
        return ProdutoSchema().dump(produto)

class CompradorResource(Resource):
    def get(self, comprador_id = None):
        if comprador_id is None:
            comprador = Comprador.query.all()
            return CompradorSchema(many=True).dump(comprador)

        comprador = Comprador.query.get(comprador_id)
        return CompradorSchema().dump(comprador)

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
        
        return CompradorSchema().dump(comprador)

    def delete(self, comprador_id = None):
        if comprador_id is None:
            abort(404, message="ID {} do Comprador não encontrado".format(comprador_id))
        Comprador.query.filter_by(id=comprador_id).delete()
        db.session.commit()

        return jsonify(msg = {
            "Resposta": "Comprador {} Deletado com Sucesso".format(comprador_id)
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
        comprador.cpf = args['cpf']

        db.session.commit()
        return CompradorSchema().dump(comprador)

class VendaResource(Resource):
    def get(self, venda_id = None):
        if venda_id is None:
            vendas = Venda.query.all()
            return VendaSchema().dump(vendas)

        venda = Venda.query.get(venda_id)
        return VendaSchema().dump(venda)

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('compradorId', type=str, required=True)
        args = parser.parse_args()

        venda = Venda(nome=args['compradorId'])

        db.session.add(venda)
        db.session.commit()
        return ClienteSchema().dump(venda)

    def put(self, venda_id=None):
        if venda_id is None:
            abort(404, message="ID {} do Venda não encontrado".format(venda_id))
        
        parser = reqparse.RequestParser()
        parser.add_argument('compradorId', type=str, required=True)
        args = parser.parse_args()

        venda = Venda.query.get(venda_id)
        venda.compradorId = args['compradorId']

        db.session.commit()
        return ClienteSchema().dump(venda)

    def delete(self, venda_id=None):
        if venda_id is None:
            abort(404, message="ID {} do Venda não encontrada".format(venda_id))
        Venda.query.filter_by(id=venda_id).delete()
        db.session.commit()

        return jsonify(msg = {
            "Resposta": "Venda {} Deletada com Sucesso".format(venda_id)
        })
        
class ItemVendasResource(Resource):
    def get(self, id=None):
        if id is None:
            itensVenda = ItensVenda.query.all()
            
            return ItensVendaSchema(many=True).dump(itensVenda)
        
        itemVenda = ItensVenda.query.get(id)
        
        return ItensVendaSchema().dump(itemVenda)

    
    
        