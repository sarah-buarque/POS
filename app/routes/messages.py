from flask import Blueprint, jsonify, request
from app.controllers.message_controller import (
    listar_mensagens,
    criar_mensagem,
    atualizar_mensagem,
    deletar_mensagem
)

messages_bp = Blueprint("messages", __name__)

@messages_bp.route("/", methods=["GET"])
def get_messages():
    return jsonify(listar_mensagens())


@messages_bp.route("/", methods=["POST"])
def post_message():
    data = request.get_json()
    response, status = criar_mensagem(data)
    return jsonify(response), status


@messages_bp.route("/<int:id>", methods=["PATCH"])
def patch_message(id):
    data = request.get_json()
    response, status = atualizar_mensagem(id, data)
    return jsonify(response), status


@messages_bp.route("/<int:id>", methods=["DELETE"])
def delete_message(id):
    response, status = deletar_mensagem(id)
    return jsonify(response), status