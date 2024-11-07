from Look4Food.backend_atualizado.database.sql_alchemy import banco

class usuarioModel(banco.Model):
    __tablename__ = 'Cliente'
    ID = banco.Column(banco.Integer, primary_key = True)
    Nome = banco.Column(banco.String(100))
    CPF = banco.Column(banco.String(14))
    email = banco.Column(banco.String(100))
    senha = banco.Column(banco.String(100))
    telefone = banco.Column(banco.String(20))
    Cidade = banco.Column(banco.String(100))
        
    def __init__(self, Nome, CPF, email, senha, telefone, Cidade):
      self.Nome = Nome
      self.CPF = CPF
      self.email = email
      self.senha = senha
      self.telefone = telefone
      self.Cidade = Cidade
      
    def json(self):
      return {
          "ID": self.ID,
          "Nome": self.Nome,
          "CPF": self.CPF,
          "email": self.email,
          "telefone": self.telefone,
          "Cidade": self.Cidade
      }
      
    @classmethod
    def find_usuario_all(cls):  
      usuarios = cls.query.select_from()
      if usuarios:
        return usuarios
      else:
        return None
      
    @classmethod
    def find_usuario(cls, ID):
      usuario = cls.query.filter_by(ID=ID).first()
      if usuario:
        return usuario
      return None
    
    @classmethod
    def find_email_usuario(cls, email):
      usuario = cls.query.filter_by(email=email).first()
      if usuario:
        return usuario
      return None
    def save_usuario(self):
      banco.session.add(self)
      banco.session.commit()
      
    def updateusuario(self, Nome, email, telefone, Cidade):
      self.Nome = Nome
      self.email = email
      self.telefone = telefone
      self.Cidade = Cidade
    
    @classmethod  
    def deleteUsuario(self, ID):
      usuario = usuarioModel.query.get(ID)
      banco.session.delete(usuario)
      banco.session.commit()
      
    @classmethod
    def buscarEmailUsuario(self, email):
      usuarios = self.query.filter_by(email=email).all()
      encontrar_email = []
      if not usuarios:
        return usuarios
      else:  
        for usuario in usuarios:
            usuario_dict = {
                "ID": usuario.ID,
                "Nome": usuario.Nome,
                "CPF": usuario.CPF,
                "email": usuario.email,
                "telefone": usuario.telefone,
                "Cidade": usuario.Cidade
            }
            encontrar_email.append(usuario_dict)
        return encontrar_email  
      
      
    @classmethod
    def findAll(self):
      clientes = self.query.all()
      lista_usuario = []

      for usuario in clientes:
          usuario_dict = {
              "ID": usuario.ID,
                "Nome": usuario.Nome,
                "CPF": usuario.CPF,
                "email": usuario.email,
                "telefone": usuario.telefone,
                "Cidade": usuario.Cidade
          }
          lista_usuario.append(usuario_dict)
      return lista_usuario
      
    @classmethod
    def updateusuario(self, ID, Nome, CPF, email, senha, telefone, Cidade):     
      usuarios = self.query.filter_by(ID=ID).first()
      if usuarios:
        # Atualiza os atributos do restaurante com base no dicionário
        usuarios.Nome = Nome
        usuarios.CPF = CPF
        usuarios.email = email
        usuarios.senha = senha
        usuarios.telefone = telefone
        usuarios.Cidade = Cidade
        banco.session.commit()
        return usuarios