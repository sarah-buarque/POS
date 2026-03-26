from app.extensions import db
from app.models.message import Message

def listar_mensagens():
    mensagens = Message.query.all()

    return {
        "mensagens": [m.to_dict() for m in mensagens]
    }


def criar_mensagem(data):
    content = data.get("content")

    if not content:
        return {"erro": "Campo 'content' é obrigatório"}, 400

    nova_mensagem = Message(content=content)

    db.session.add(nova_mensagem)
    db.session.commit()

    return nova_mensagem.to_dict(), 201