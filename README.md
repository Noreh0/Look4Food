<h1>Look4Food - Padrões de Projeto e Multicamadas Trabalho Final</h1>

# 1 - Código – Main - Refatorado com o Padrão Factory Pattern

Primeiro, organizaremos o código em uma estrutura de pastas que ajuda a manter os arquivos organizados:
project/

│

├── app/

│ ├── __init__.py           # Arquivo de inicialização para o padrão Factory

│
├── routes.py             # Definindo as rotas separadamente

│
├── extensions.py         # Configuração de extensões como JWT, CORS, etc.

│
└── config.py             # Configuração do app, banco de dados, etc.

│
├── main.py                   # Arquivo principal para executar o app

└── resource/                 # Suas rotas de recursos

Arquivo __init__.py (Definição do Factory)
No __init__.py, vamos criar a função create_app, que será responsável por configurar e retornar a instância do app Flask.

![image](https://github.com/user-attachments/assets/2c4387e6-04ea-4a49-8b7b-73de1ee4c7f4)

Arquivo config.py (Configurações do App)
Este arquivo define as configurações do aplicativo em um único local, como a URL do banco de dados e a chave secreta para o JWT.

![image](https://github.com/user-attachments/assets/60a485a9-fe1b-4f3b-ae25-330c1122e7da)

Arquivo extensions.py (Extensões do Flask)
Separar as extensões como JWT, CORS, e SQLAlchemy ajuda a manter o código organizado e fácil de configurar.

![image](https://github.com/user-attachments/assets/ff1ab05b-25e0-45f4-bfb4-bfb6308b0a10)

Arquivo routes.py (Definindo as Rotas)
Definimos todas as rotas em um único arquivo e as registramos no app principal através da função register_routes.

![image](https://github.com/user-attachments/assets/bd671692-bb67-4016-942c-e8562b026f2d)

Arquivo main.py (Ponto de Entrada)
Agora, o arquivo principal só precisa criar o app e rodá-lo. Isso ajuda a manter o ponto de entrada bem limpo e organizado.

![image](https://github.com/user-attachments/assets/3ff273b8-b2e7-4f88-858c-3d57c244d37e)

Conclusão:
Padrão Factory: A função create_app no __init__.py encapsula a criação e configuração do app, tornando-o modular e reutilizável.
Separação de Configurações: O config.py organiza as configurações, facilitando mudanças.
Extensões Centralizadas: O extensions.py centraliza as instâncias de extensões como db (SQLAlchemy) e jwt (JWTManager), permitindo fácil modificação e inicialização.
Rotas Organizadas: O routes.py define e registra as rotas em um único local, o que facilita a leitura e manutenção.

# 2 - Padrão de projeto - Facade Pattern
Com o Facade Pattern, criamos uma classe UsuarioFacade que simplifica as operações do usuário (find, save, update, etc.) usando os métodos existentes na sua classe usuario Model(usuarioModel), escondendo a complexidade das operações com o banco.

![image](https://github.com/user-attachments/assets/5ff0d524-0ef7-419f-b6a9-c93017e51bed) 

# 3 - Padrão de projeto - Factory Pattern
O Factory Pattern pode ser aplicado para criar instâncias, com o exemplo do restauranteModel, encapsulamos a lógica de criação. Isso pode ser útil, especialmente se houver diferentes maneiras de criar um restaurante.

![image](https://github.com/user-attachments/assets/9a6346e2-ab4f-4aa7-aa23-3014174a85ce)

# 4 - Padrão de projeto Singleton para um Gerenciador de Avaliações
Garante que exista apenas uma instância de um recurso compartilhado, como um "gerenciador" de avaliações. Este gerenciador poderia centralizar a manipulação de avaliações e garantir que sempre retornemos a mesma instância, seja para gerenciar avaliações ou realizar operações frequentes com o banco de dados.

![image](https://github.com/user-attachments/assets/c3b71409-0c65-4058-bb80-f9988a0decd2)

# 5 - Exemplo do Padrão de Projeto Builder
Vamos usar o Builder para construir o objeto de avaliacao (avaliacao Model) com seus campos, em vez de passar todos os parâmetros diretamente ao instanciar o modelo.
1. Criação do Builder
Criaremos uma classe AvaliacaoBuilder que permitirá definir cada campo gradualmente, chamando métodos que configuram atributos específicos da avaliação. No final, um método build() retorna a avaliação construída.

![image](https://github.com/user-attachments/assets/bdf8733c-af30-41ec-812a-9748c0794310)

Essa classe AvaliacaoBuilder permite que você crie uma avaliação (avaliacaoModel) de forma incremental, adicionando dados de maneira opcional conforme necessário.

2. Uso do Builder nas Classes de Recurso
Agora, usamos o AvaliacaoBuilder nos endpoints para construir a avaliação antes de salvá-la ou atualizá-la. Isso melhora a clareza e a flexibilidade ao criar ou modificar instâncias de avaliacaoModel.

![image](https://github.com/user-attachments/assets/6461a217-dc0c-43cd-bfe9-72c8d18777ab)

3. Exemplo com Atualização de Avaliação
No caso de atualizar uma avaliação existente, você pode modificar apenas os campos necessários usando o Builder:

![image](https://github.com/user-attachments/assets/04231a5b-9864-4578-b194-44787152907b)

 
Vantagens do Uso do Builder no Código
1.	Flexibilidade: Constrói objetos com apenas os campos necessários e evita a criação de construtores muito longos com muitos parâmetros.
2.	Leitura: Deixa o código mais legível, pois os campos são configurados explicitamente com métodos descritivos (with_nota, with_comentario).
3.	Manutenção: Se novos campos forem adicionados, é fácil atualizar o AvaliacaoBuilder sem modificar as chamadas em vários lugares do código.
   
<h2>Heron Ricardo</h2>
