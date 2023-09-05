# Imports
from flask import Flask, render_template
from flask_restful import Api
from models import db, ma
from resources import ClienteResource, ProdutoResource, CompradorResource, VendaResource

# Config
app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
api = Api(app)
db.init_app(app)
ma.init_app(app)

# Create DB
with app.app_context():
    db.create_all()

# Routes
api.add_resource(ClienteResource, '/cliente', '/cliente/<int:cliente_id>')
api.add_resource(ProdutoResource, '/produto', '/produto/<int:produto_id>')
api.add_resource(CompradorResource, '/comprador', '/comprador/<int:comprador_id>')
api.add_resource(VendaResource, '/venda', '/venda/<int:venda_id>')

# Initi APP
if __name__ == '__main__':
    app.run(debug=True)
    