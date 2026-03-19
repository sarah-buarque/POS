from flask import Flask, jsonify
from app import create_app

app = create_app()
app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"mensagem": "Olá, mundo!"})

@app.route("/mensagens", methods={"GET"})
def listar_mensagens():
    return jsonify({
        "mensagens": [
            "Primeira mensagem",
            "Segunda mensagem"
            ]
            })

@app.route("/mensagens", methods={"POST"})
def criar_mensagens():
    return jsonify({
        "mensagens": [
            "1a mensagem",
            "2a mensagem"
            ]
            })