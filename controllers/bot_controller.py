from flask import Blueprint, jsonify, request

from chatbot.chatbot_conversas import chatterbot, chatbot_config

chat_bp = Blueprint('chat', __name__, url_prefix='/gupy')


# fluxo de mensagens do chatbot
@chat_bp.route('/get_job_messages', methods=['POST'])
def get_job_messages():
    data = request.get_json()
    pergunta = data.get('pergunta')

    resposta = chatbot_config.obter_resposta(pergunta)

    return jsonify({'resposta': resposta})

