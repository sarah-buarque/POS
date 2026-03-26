from flask import Blueprint, jsonify, request
from app.controllers.message_controller import (
    listar_mensagens,
    criar_mensagem
)

messages_bp = Blueprint("messages", __name__)

@messages_bp.route("/", methods=["GET"])
def get_messages():
    data = listar_mensagens()
    return jsonify(data)


@messages_bp.route("/", methods=["POST"])
def post_message():
    data = request.get_json()

    response, status = criar_mensagem(data)

    return jsonify(response), status