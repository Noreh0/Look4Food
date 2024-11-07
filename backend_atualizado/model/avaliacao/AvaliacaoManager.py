from Look4Food.backend_atualizado.model.avaliacao.avaliacao import avaliacaoModel


class AvaliacaoManager:
  # Atributo de classe para armazenar a instância única
    _instance = None  
    # Inicialização adicional pode ser feita aqui, se necessário
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(AvaliacaoManager, cls).__new__(cls)
        return cls._instance
    def get_avaliacao(self, ID):
        """Método para buscar uma avaliação específica."""
        return avaliacaoModel.find_avaliacoes(ID)
    def salvar_avaliacao(self, nota, comentario, id_cliente, id_restaurante):
        """Método para salvar uma nova avaliação."""
        nova_avaliacao = avaliacaoModel(nota, comentario, id_cliente, id_restaurante)
        nova_avaliacao.save_avaliacoes()
        return nova_avaliacao.json()
    def deletar_avaliacao(self, ID):
        """Método para deletar uma avaliação específica."""
        avaliacaoModel.delete_avaliacao(ID)
    def listar_todas_avaliacoes(self):
        """Método para listar todas as avaliações."""
        return avaliacaoModel.findAll()
# Uso do Singleton AvaliacaoManager
gerenciador1 = AvaliacaoManager()
gerenciador2 = AvaliacaoManager()

print(gerenciador1 is gerenciador2)  # Output: True, ambos são a mesma instância

# Usando o gerenciador para buscar, salvar ou deletar avaliações
avaliacao = gerenciador1.get_avaliacao(ID=1)
nova_avaliacao = gerenciador1.salvar_avaliacao(5, "Ótimo restaurante!", 101, 202)
gerenciador1.deletar_avaliacao(ID=2)
