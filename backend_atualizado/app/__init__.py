from flask import Flask
from .extensions import jwt, cors, db
from .config import Config
from .routes import register_routes

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializando extensões
    cors.init_app(app)
    jwt.init_app(app)
    db.init_app(app)

    # Registrando rotas
    register_routes(app)

    # Criação do banco de dados antes de cada requisição
    @app.before_first_request
    def create_database():
        db.create_all()

    return app
