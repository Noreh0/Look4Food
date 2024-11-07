from Look4Food.backend_atualizado.database.sql_alchemy import banco
from Look4Food.backend_atualizado.model.usuario.usuario import usuarioModel

class UsuarioFacade:
    @staticmethod
    def criar_usuario(nome, cpf, email, senha, telefone, cidade):
        usuario = usuarioModel(nome, cpf, email, senha, telefone, cidade)
        usuario.save_usuario()
        return usuario

    @staticmethod
    def buscar_usuario_por_id(id_usuario):
        return usuarioModel.find_usuario(id_usuario)

    @staticmethod
    def buscar_usuario_por_email(email):
        return usuarioModel.find_email_usuario(email)

    @staticmethod
    def atualizar_usuario(id_usuario, nome, cpf, email, senha, telefone, cidade):
        usuario = usuarioModel.find_usuario(id_usuario)
        if usuario:
            usuario.updateusuario(nome, email, telefone, cidade)
            usuario.save_usuario()
            return usuario
        return None

    @staticmethod
    def deletar_usuario(id_usuario):
        return usuarioModel.deleteUsuario(id_usuario)

