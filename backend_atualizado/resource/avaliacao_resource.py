from flask import Flask, jsonify
from flask_restx import Resource, reqparse
from models.avaliacao import avaliacaoModel
from flask_jwt_extended import jwt_required


class Avaliacoes(Resource):
  def get(self):
    return{'avaliacoes': [avaliacao.json() for avaliacao in avaliacaoModel.query.all()]}
class Avaliacao(Resource):
  argumentos = reqparse.RequestParser()
  argumentos.add_argument('Nota', type=str, required=True, help="O campo 'Nota' nao pode ser deixado em branco!")
  argumentos.add_argument('Comentario', type=str, required=True, help="Por favor adicione um 'Comentario'")
  argumentos.add_argument('ID_Cliente', type=int, required=True)
  argumentos.add_argument('ID_Restaurante', type=int, required=True)
  
  def get(self, ID):
    avaliacao = avaliacaoModel.find_avaliacoes(ID)
    if avaliacao:
      return avaliacao.json()
    return{'message': 'Avaliacao not found.'}, 404 # not found
    
  """@jwt_required()""" 
  def delete(self, ID):
    avaliacoes = avaliacaoModel.find_avaliacoes(ID)
    if avaliacoes:
      try:
        avaliacoes.avaliacoes_delete()
      except:
        return {'massage': 'An error ocurred trying to delete avaliacao!'}, 500  
      return {'message': 'Avaliação deletada!'}
    return {'message': 'Avaliacao not found!'}, 400

class remover_avaliacao(Resource):
  def delete(self, ID):
    avaliacaoModel.delete_avaliacao(ID)  

class editarAvaliacao(Resource):
  def put(self, ID):
    dados = Avaliacao.argumentos.parse_args()
    avaliacao = avaliacaoModel(**dados)    
    avaliacao.updateAvaliacao(ID, **dados)
    return avaliacao.json()
  
class criarAvaliacao(Resource):
  def post(self):
    dados = Avaliacao.argumentos.parse_args()
    avaliacao = avaliacaoModel(**dados)
    avaliacao.save_avaliacoes()
  
class encontrarAvaliacao(Resource):
  def get(self, ID_Restaurante):
    listar = avaliacaoModel.findAllAvaliacoes(ID_Restaurante)
    return listar

class allAvaliacoes(Resource):
  def get(self):
    listar = avaliacaoModel.findAll()
    return listar
   
class encontrarAvaliacaoCliente(Resource):
  def get(self, ID_Cliente):
    listar = avaliacaoModel.findAllCliente(ID_Cliente)
    return listar
