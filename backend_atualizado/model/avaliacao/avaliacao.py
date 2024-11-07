import resource
from Look4Food.backend_atualizado.database.sql_alchemy import banco
from Look4Food.backend_atualizado.model.avaliacao.avaliacaoBuilder import AvaliacaoBuilder
from Look4Food.backend_atualizado.resource.avaliacao_resource import Avaliacao

class criarAvaliacao(resource):
    def post(self):
        dados = Avaliacao.parse_args()  # Usando DTO para validar dados

        # Usando o Builder para construir a avaliação
        avaliacao = (AvaliacaoBuilder()
                     .with_nota(dados['Nota'])
                     .with_comentario(dados['Comentario'])
                     .with_id_cliente(dados['ID_Cliente'])
                     .with_id_restaurante(dados['ID_Restaurante'])
                     .build())

        avaliacao.save_avaliacoes()
        return avaliacao.json(), 201

class editarAvaliacao(resource):
    def put(self, ID):
        dados = Avaliacao.parse_args()

        # Atualiza a avaliação existente, configurando apenas os campos fornecidos
        avaliacao = Avaliacao.find_avaliacao_by_id(ID)
        if not avaliacao:
            return {'message': 'Avaliacao not found!'}, 404

        # Usando Builder para atualizar campos específicos
        avaliacao = (AvaliacaoBuilder()
                     .with_nota(dados['Nota'] if 'Nota' in dados else avaliacao.Nota)
                     .with_comentario(dados['Comentario'] if 'Comentario' in dados else avaliacao.Comentario)
                     .with_id_cliente(dados['ID_Cliente'] if 'ID_Cliente' in dados else avaliacao.ID_Cliente)
                     .with_id_restaurante(dados['ID_Restaurante'] if 'ID_Restaurante' in dados else avaliacao.ID_Restaurante)
                     .build())
                     
        avaliacao.updateAvaliacao(ID, **dados)
        return avaliacao.json()



class avaliacaoModel(banco.Model):
    __tablename__ = 'Avaliacao'

    ID = banco.Column(banco.Integer, primary_key = True)
    Comentario = banco.Column(banco.String())
    Nota = banco.Column(banco.Integer)
    ID_Cliente = banco.Column(banco.Integer)
    ID_Restaurante = banco.Column(banco.Integer)
    
    def __init__(self, Nota, Comentario, ID_Cliente, ID_Restaurante):
      self.Comentario = Comentario
      self.Nota = Nota
      self.ID_Cliente = ID_Cliente
      self.ID_Restaurante = ID_Restaurante
      
    def json(self):
      return {
          "ID": self.ID,
          "Comentario": self.Comentario,
          "Nota": self.Nota,
          "ID_Cliente": self.ID_Cliente,
          "ID_Restaurante": self.ID_Restaurante
      }
      
    @classmethod
    def find_avaliacoes(cls, ID):
      avaliacao = cls.query.filter_by(ID=ID).first()
      if avaliacao:
        return avaliacao
      return None
    def save_avaliacoes(self):
      banco.session.add(self)
      banco.session.commit()
      
    
    @classmethod
    def updateAvaliacao(self, ID, Nota, Comentario, ID_Cliente, ID_Restaurante):     
      avaliacao = self.query.filter_by(ID=ID).first()
      if avaliacao:
        # Atualiza os atributos do restaurante com base no dicionário
        avaliacao.Nota = Nota
        avaliacao.Comentario = Comentario
        avaliacao.ID_Cliente = ID_Cliente
        avaliacao.ID_Restaurante = ID_Restaurante
        
        banco.session.commit()
        return avaliacao
    
    
    @classmethod
    def findAll(self):
      avaliacoes = self.query.all()
      lista_de_avaliacao = []

      for avaliacao in avaliacoes:
          avaliacao_dict = {
              "ID": avaliacao.ID,
              "Comentario": avaliacao.Comentario,
              "Nota": avaliacao.Nota,
              "ID_Cliente": avaliacao.ID_Cliente,
              "ID_Restaurante": avaliacao.ID_Restaurante
          }
          lista_de_avaliacao.append(avaliacao_dict)
      return lista_de_avaliacao
    
    @classmethod
    def findAllAvaliacoes(cls, ID_Restaurante):
      avaliacoes = cls.query.filter_by(ID_Restaurante=ID_Restaurante).all()
      lista_de_avaliacao = []

      for avaliacao in avaliacoes:
          avaliacao_dict = {
              "ID": avaliacao.ID,
              "Comentario": avaliacao.Comentario,
              "Nota": avaliacao.Nota,
              "ID_Cliente": avaliacao.ID_Cliente,
              "ID_Restaurante": avaliacao.ID_Restaurante
          }
          lista_de_avaliacao.append(avaliacao_dict)
      return lista_de_avaliacao
    
    @classmethod
    def findAllCliente(cls, ID_Cliente):
      avaliacoes = cls.query.filter_by(ID_Cliente=ID_Cliente).all()
      lista_de_avaliacao = []

      for avaliacao in avaliacoes:
          avaliacao_dict = {
              "ID": avaliacao.ID,
              "Comentario": avaliacao.Comentario,
              "Nota": avaliacao.Nota,
              "ID_Cliente": avaliacao.ID_Cliente,
              "ID_Restaurante": avaliacao.ID_Restaurante
          }
          lista_de_avaliacao.append(avaliacao_dict)
      return lista_de_avaliacao
    @classmethod
    def buscarAvaliacao(cls, ID):
      avaliacoes = cls.query.filter_by(ID=ID).all()
      lista_de_avaliacao = []
      for avaliacao in avaliacoes:
          avaliacao_dict = {
              "ID": avaliacao.ID,
              "Comentario": avaliacao.Comentario,
              "Nota": avaliacao.Nota,
              "ID_Cliente": avaliacao.ID_Cliente,
              "ID_Restaurante": avaliacao.ID_Restaurante
          }
          lista_de_avaliacao.append(avaliacao_dict)
      return lista_de_avaliacao 
    
    
    @classmethod
    def findandremove(cls, ID_Restaurante):
      avaliacoes = cls.query.filter_by(ID_Restaurante=ID_Restaurante).all()

      for avaliacao in avaliacoes:
          avaliacao_dict = {
              "ID": avaliacao.ID,
              "Comentario": avaliacao.Comentario,
              "Nota": avaliacao.Nota,
              "ID_Cliente": avaliacao.ID_Cliente,
              "ID_Restaurante": avaliacao.ID_Restaurante
          }
          avaliacao_teste = avaliacaoModel.query.get(avaliacao_dict.get("ID"))
          banco.session.delete(avaliacao_teste)
          
