# Builder para construir uma instância de avaliação com diferentes parâmetros
from Look4Food.backend_atualizado.model.avaliacao.avaliacao import avaliacaoModel


class AvaliacaoBuilder:
    def __init__(self):
        self.dados = {}

    def with_nota(self, nota):
        self.dados['Nota'] = nota
        return self

    def with_comentario(self, comentario):
        self.dados['Comentario'] = comentario
        return self

    def with_id_cliente(self, id_cliente):
        self.dados['ID_Cliente'] = id_cliente
        return self

    def with_id_restaurante(self, id_restaurante):
        self.dados['ID_Restaurante'] = id_restaurante
        return self

    def build(self):
        return avaliacaoModel(**self.dados)
