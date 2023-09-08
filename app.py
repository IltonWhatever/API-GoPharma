# Imports
from flask import Flask, render_template
from flask_restful import Api
from models import db, ma
from resources import ClienteResource, ProdutoResource, CompradorResource, VendaResource, ItemVendasResource
from flask_swagger_ui import get_swaggerui_blueprint


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
api.add_resource(ItemVendasResource, '/itens-venda', '/itens-venda/<int:item_venda_id>')

# Configure Swagger UI
SWAGGER_URL = '/swagger'
API_URL = 'http://localhost:5000/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Sample API"
    }
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

@app.route('/swagger.json')
def swagger():
    with open('swagger.json', 'r') as f:
        return jsonify(json.load(f))


# Initi APP
if __name__ == '__main__':
    app.run(debug=True)
    