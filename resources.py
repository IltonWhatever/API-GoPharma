# Resources
from flask_restful import Resource, reqparse, abort
from flask import jsonify
from models import db,Cliente,ClienteSchema

class ClienteResource(Resource):
    def get(self, cliente_id=None):
        if cliente_id is None:
            cliente = Cliente.querry.all()
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