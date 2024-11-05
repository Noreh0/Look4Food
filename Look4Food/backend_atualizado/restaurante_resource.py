from flask import Flask, jsonify 
from flask_restx import Resource, reqparse
from models.restaurante import restauranteModel
from models.avaliacao import avaliacaoModel
from flask_jwt_extended import create_access_token, jwt_required, get_jwt
import hmac
import json
'''from blacklist import BLACKLIST
'''
def safe_str_cmp(email: str, senha: str) -> bool:
      return hmac.compare_digest(email, senha)
    
atributos = reqparse.RequestParser()
atributos.add_argument('Nome', type=str, required=True, help="O campo 'Nome' nao pode ser deixado em branco!")
atributos.add_argument('CNPJ', type=str, required=True, help="Não deixar o campo 'CNPJ' em branco.")
atributos.add_argument('email', type=str, required=True, help="Adicione um 'email'.")
atributos.add_argument('senha', type=str, required=True, help="O campo 'senha' deve ser preenchido.")
atributos.add_argument('telefone', type=str, required=True, help="Coloque seu 'telefone'.")
atributos.add_argument('Endereco', type=str, required=True, help="Coloque seu 'Endereco'.")
atributos.add_argument('Cidade', type=str, required=True, help="Adicione sua 'Cidade'.")
atributos.add_argument('tipo_restaurante', type=str, required=True, help="Qual o tipo do seu restaurante'?")
atributos.add_argument('descricao', type=str, required=True, help="Descreva seu restaurante'?")


login = reqparse.RequestParser()
login.add_argument('email', type=str, required=True, help="Adicione um 'email'.")
login.add_argument('senha', type=str, required=True, help="O campo 'senha' deve ser preenchido.")


class Restaurante(Resource):
  def get(self, ID):
    restaurante = restauranteModel.find_restaurante(ID)
    if restaurante:
      return restaurante
    return{'message': 'Restaurante not found.'}, 404 # not found 
     
  
class remover_restaurante(Resource):
  def delete(self, ID):
    avaliacaoModel.findandremove(ID)
    restauranteModel.delete_restaurante(ID)
    
class tipo_restaurante(Resource):
  def get(self):
    restaurante = restauranteModel.find_tipo_restaurante()
    if restaurante:
      return restaurante.json()
    return{'message': 'Restaurante not found.'}, 404 # not found
  
class listar_restaurantes(Resource):
  def get(self):
    listar = restauranteModel.find_all_restaurante()
    if listar:
      return listar
    else:
      return{"message": "Nenhum restaurante encontrado"}, 400
    
class filtrar_restaurante(Resource):
  def get(self, tipo_restaurante):
    listar = restauranteModel.find_all_restaurante()
    if tipo_restaurante == "Nenhum":
      return listar
    else:
      filtrar = restauranteModel.find_tipo_restaurante(tipo_restaurante)
      return filtrar
    
class buscarRestaurante(Resource):
  def get(self, email):
    buscar = restauranteModel.find_email_restaurante(email)
    return buscar
  
class encontrarEmailRes(Resource):
  def get(self, email):
    buscarEmailRes = restauranteModel.buscar_email_restaurante(email)
    return buscarEmailRes
  
class cadastroRestaurante(Resource): 
  def post(self):
    dados = atributos.parse_args()
    if restauranteModel.find_email_restaurante(dados['email']):
      return{"message": "The email'{}' already exists".format(dados['email'])}
    else:
      restaurante = restauranteModel(**dados)
      restaurante.save_restaurante()
      return {"message": "restaurante criado com sucesso!"}, 201
    
class editarRestaurante(Resource):
  def put(self, ID):
    dados = atributos.parse_args()
    restaurante = restauranteModel(**dados)    
    restaurante.updaterestaurante(ID, **dados)
    return restaurante.json()
    
class loginrestaurante(Resource):
  @classmethod
  def post(self):
    dados = login.parse_args()
    restaurante = restauranteModel.find_email_restaurante(dados['email'])
    if restaurante and safe_str_cmp(restaurante.senha, dados['senha']):
      token_de_acesso = create_access_token(identity = restaurante.email)
      return token_de_acesso       
    return {'message': 'The username or the password is incorrect'}, 401
    
class logoutRestaurante(Resource):
  def post(self):
    return {'message': 'voce foi deslogado!'}
  
  
class pesquisar(Resource):
  def get(self, Nome):
    restaurante = restauranteModel.find_name_restaurante(Nome)
    return restaurante