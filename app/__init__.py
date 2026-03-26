from flask import Flask
from .config import Config
from .extensions import db, migrate, ma
from .routes.messages import messages_bp
from marshmallow import ValidationError
from werkzeug.exceptions import NotFound

def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)

    from .models import message

    app.register_blueprint(messages_bp, url_prefix="/messages")

    @app.errorhandler(ValidationError)
    def handle_validation_error(err):
        return {"errors": err.messages}, 400

    @app.errorhandler(NotFound)
    def handle_not_found(err):
        return {"erro": "Recurso não encontrado"}, 404

    return app