from Look4Food.backend_atualizado.resource.avaliacao_resource import Avaliacoes, Avaliacao, criarAvaliacao, encontrarAvaliacao, encontrarAvaliacaoCliente, remover_avaliacao ,editarAvaliacao, allAvaliacoes
from Look4Food.backend_atualizado.resource.usuario_resource import Usuario, cadastroCliente, loginUsuario, logoutUsuario, buscarUsuario, encontrarEmail, editarUsuario, removerUsuario, allClientes
from Look4Food.backend_atualizado.resource.restaurante_resource import Restaurante, cadastroRestaurante, loginrestaurante, logoutRestaurante, tipo_restaurante, listar_restaurantes, filtrar_restaurante, pesquisar, buscarRestaurante, encontrarEmailRes, editarRestaurante, remover_restaurante
from flask_restx import Api


api = Api(version='1.0', title='API de Exemplo', description='Uma API de exemplo usando Flask-RESTX para OpenAPI')

def register_routes(app):
    api.init_app(app)

    # Rotas de Avaliação
    api.add_resource(Avaliacoes, '/avaliacoes')
    api.add_resource(Avaliacao, '/avaliacoes/<int:ID>')
    api.add_resource(allAvaliacoes, '/todasAvaliacoes')
    api.add_resource(editarAvaliacao, '/editarAvaliacao/<int:ID>')
    api.add_resource(remover_avaliacao, '/excluirAvaliacao/<int:ID>')
    api.add_resource(criarAvaliacao, '/avaliando')
    api.add_resource(encontrarAvaliacao, '/encontraAvaliacao/<int:ID_Restaurante>')
    api.add_resource(encontrarAvaliacaoCliente, '/encontraAvaliacaoCliente/<int:ID_Cliente>')

    # Rotas de Usuario
    api.add_resource(Usuario, '/cliente/<int:ID>')
    api.add_resource(allClientes, '/todosClientes')
    api.add_resource(cadastroCliente, '/cadastroCliente')
    api.add_resource(removerUsuario, '/excluirCliente/<int:ID>')
    api.add_resource(editarUsuario, '/editarCliente/<int:ID>')
    api.add_resource(loginUsuario, '/login')
    api.add_resource(logoutUsuario, '/logout')
    api.add_resource(buscarUsuario, '/buscarUsuario/<string:email>')
    api.add_resource(encontrarEmail, '/encontrarUsuario/<string:email>')

    # Rotas de Restaurante
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
    api.add_resource(encontrarEmailRes, '/encontrarRestaurante/<string:email>')
    api.add_resource(editarRestaurante, '/editarRestaurante/<int:ID>')
