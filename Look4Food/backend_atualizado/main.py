from flask import Flask, jsonify, render_template, request
"""from flask_restful import Api"""
from resource.avaliacao import Avaliacoes, Avaliacao, criarAvaliacao, encontrarAvaliacao, encontrarAvaliacaoCliente, remover_avaliacao ,editarAvaliacao, allAvaliacoes
from resource.usuario import Usuario, cadastroCliente, loginUsuario, logoutUsuario, buscarUsuario, encontrarEmail, editarUsuario, removerUsuario, allClientes
from resource.restaurante import Restaurante, cadastroRestaurante, loginrestaurante, logoutRestaurante, tipo_restaurante, listar_restaurantes, filtrar_restaurante, pesquisar, buscarRestaurante, encontrarEmailRes, editarRestaurante, remover_restaurante
from flask_jwt_extended import JWTManager
from blacklist import BLACKLIST
from flask_cors import CORS
from flask_restx import Api, Resource
import yaml
import mariadb

app = Flask(__name__)
cors = CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mariadb://root:L23092004@192.168.1.102:2321/ExpCriativaapp'
"""ExpCriativaapp@24"""
app.config['JWT_SECRET_KEY'] = 'SENHA SEGURA, NÃO COMPARTILHE'
app.config['JWT_BLACKLIST_ENABLE'] = True
"""api = Api(app)"""
jwt = JWTManager(app)

api = Api(app, version='1.0', title='API de Exemplo', description='Uma API de exemplo usando Flask-RESTX para OpenAPI')
with open('openapi.yaml', 'r') as yamlfile:
    cfg = yaml.safe_load(yamlfile)

api.add_resource(Restaurante, '/restaurante', endpoint='Restaurante_open')
api.add_resource(cadastroRestaurante, '/cadastroRestaurante', endpoint='cadastroRestaurante_open')
api.add_resource(tipo_restaurante, '/tipo_restaurante', endpoint='tipo_restaurante_open')
api.add_resource(listar_restaurantes, '/menu', endpoint='listar_restaurantes_open')
api.add_resource(filtrar_restaurante, '/filtrar/<string:tipo_restaurante>', endpoint='filtrar_restaurante_open')
api.add_resource(buscarRestaurante, '/buscarRestaurante/<string:email>', endpoint='buscarRestaurante_open')
api.add_resource(buscarUsuario, '/buscarUsuario/<string:email>', endpoint='buscarUsuario_open')
api.add_resource(encontrarEmail, '/encontrarUsuario/<string:email>', endpoint='encontrarEmail_open')
api.add_resource(encontrarEmailRes, '/encontrarRestaurante/<string:email>', endpoint='encontrarEmailRes_open')
api.add_resource(editarRestaurante, '/editarRestaurante/<int:ID>', endpoint='editarRestaurante_open')
api.add_resource(encontrarAvaliacao, '/encontraAvaliacao/<int:ID_Restaurante>', endpoint='encontrarAvaliacao_open')

@app.before_request
def createDatabase():
  banco.create_all() 

@jwt.token_in_blocklist_loader
def verifica_blacklist(self, token):
  return token['jti'] in BLACKLIST

@jwt.revoked_token_loader
def token_acesso_invalido(jwt_header, jwt_payload):
  return jsonify({'message': 'voce ja se realizou logout'}), 401


api.add_resource(Avaliacoes, '/avaliacoes')
api.add_resource(Avaliacao, '/avaliacoes/<int:ID>')
api.add_resource(allAvaliacoes, '/todasAvaliacoes')
api.add_resource(editarAvaliacao, '/editarAvaliacao/<int:ID>')
api.add_resource(remover_avaliacao, '/excluirAvaliacao/<int:ID>')
api.add_resource(criarAvaliacao, '/avaliando')
api.add_resource(Usuario, '/cliente/<int:ID>')
api.add_resource(allClientes, '/todosClientes')
api.add_resource(cadastroCliente, '/cadastroCliente')
api.add_resource(removerUsuario, '/excluirCliente/<int:ID>')
api.add_resource(editarUsuario, '/editarCliente/<int:ID>')
api.add_resource(loginUsuario, '/login')
api.add_resource(logoutUsuario, '/logout')
api.add_resource(Restaurante, '/restaurante/<int:ID>')
api.add_resource(cadastroRestaurante, '/cadastroRestaurante')
api.add_resource(remover_restaurante, '/excluirRestaurante/<int:ID>')
api.add_resource(loginrestaurante, '/loginRestaurante')
api.add_resource(logoutRestaurante, '/logoutRestaurante')
api.add_resource(tipo_restaurante, '/tipo_restaurante')
api.add_resource(listar_restaurantes, '/menu')
api.add_resource(filtrar_restaurante, '/filtrar/<string:tipo_restaurante>')
api.add_resource(buscarRestaurante, '/buscarRestaurante/<string:email>')
api.add_resource(pesquisar, '/pesquisarRestaurante/<string:Nome>')
api.add_resource(buscarUsuario, '/buscarUsuario/<string:email>')
api.add_resource(encontrarEmail, '/encontrarUsuario/<string:email>')
api.add_resource(encontrarEmailRes, '/encontrarRestaurante/<string:email>')
api.add_resource(editarRestaurante, '/editarRestaurante/<int:ID>')
api.add_resource(encontrarAvaliacao, '/encontraAvaliacao/<int:ID_Restaurante>')
api.add_resource(encontrarAvaliacaoCliente, '/encontraAvaliacaoCliente/<int:ID_Cliente>')


if __name__ == '__main__':
  from sql_alchemy import banco
  banco.init_app(app)
  app.run(debug=True)


if __name__ == '__main__':
  from sql_alchemy import banco
  banco.init_app(app)
  app.run(debug=True)
