from flask import Flask, flash, session
from flask_restx import Resource, reqparse
from models.usuario import usuarioModel
from flask_jwt_extended import create_access_token, jwt_required, get_jwt
import hmac
'''from blacklist import BLACKLIST
'''
def safe_str_cmp(email: str, senha: str) -> bool:
      return hmac.compare_digest(email, senha)
    
atributos = reqparse.RequestParser()
atributos.add_argument('Nome', type=str, required=True, help="O campo 'Nome' nao pode ser deixado em branco!")
atributos.add_argument('CPF', type=str, required=True, help="Não deixar o campo 'CPF' em branco.")
atributos.add_argument('email', type=str, required=True, help="Adicione um 'email'.")
atributos.add_argument('senha', type=str, required=True, help="O campo 'senha' deve ser preenchido.")
atributos.add_argument('telefone', type=str, required=True, help="Coloque seu 'telefone'.")
atributos.add_argument('Cidade', type=str, required=True, help="Adicione sua 'Cidade'.")


login = reqparse.RequestParser()
login.add_argument('email', type=str, required=True, help="Adicione um 'email'.")
login.add_argument('senha', type=str, required=True, help="O campo 'senha' deve ser preenchido.")


class Usuario(Resource):
  def get(self, ID):
    usuario = usuarioModel.find_usuario(ID)
    if usuario:
      return usuario.json()
    return{'message': 'Usuario not found.'}, 404 # not found    
  
   

class cadastroCliente(Resource): 
  def post(self):
    dados = atributos.parse_args()
    
    if usuarioModel.find_email_usuario(dados['email']):
      return{"message": "The email'{}' already exists".format(dados['email'])}
    else:
      usuario = usuarioModel(**dados)
      usuario.save_usuario()
      return {"message": "Usuario criado com sucesso!"}, 201

class removerUsuario(Resource):
  def delete(self, ID):
    usuarioModel.deleteUsuario(ID)

class editarUsuario(Resource):
  def put(self, ID):
    dados = atributos.parse_args()
    usuario = usuarioModel(**dados)    
    usuario.updateusuario(ID, **dados)
    return usuario.json()

class buscarUsuario(Resource):
  def get(self, email):
    buscar = usuarioModel.find_email_usuario(email)
    return buscar
  
class allClientes(Resource):
  def get(self):
    listar = usuarioModel.findAll()
    return listar
    
class loginUsuario(Resource):
  def post(cls):
    dados = login.parse_args()
    usuario = usuarioModel.find_email_usuario(dados['email'])
    if usuario and safe_str_cmp(usuario.senha, dados['senha']):
      token_de_acesso = create_access_token(identity = usuario.email)
      return token_de_acesso         
    return {'message': 'The username or the password is incorrect'}, 401

class encontrarEmail(Resource):
  def get(self, email):
    buscarEmail = usuarioModel.buscarEmailUsuario(email)
    return buscarEmail

class logoutUsuario(Resource):
  @jwt_required()
  def post(self):
    jwt_id = get_jwt()['jti']
    BLACKLIST.add(jwt_id)
    return {'message': 'voce foi deslogado!'}