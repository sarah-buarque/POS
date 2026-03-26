from flask import Flask
from .config import Config
from .extensions import db, migrate
from .routes.messages import messages_bp

def create_app():
    app = Flask(__name__)

    # carregar configurações
    app.config.from_object(Config)

    # inicializar extensões
    db.init_app(app)
    migrate.init_app(app, db)

    # importar modelos (necessário para migrações)
    from .models import message

    # registrar blueprints
    app.register_blueprint(messages_bp, url_prefix="/messages")

    @app.route("/", methods=["GET"])
    def home():
        return {"status": "ok", "message": "API POS funcionando"}

    return app