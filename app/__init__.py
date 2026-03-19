from flask import Flask
from .routes.messages import messages_bp

def create_app():
    app = Flask(__name__)

    app.register_blueprint(messages_bp, url_prefix="/messages")
gg
    return app