from flask import Blueprint, jsonify, request, Response, session
import json

from chatbot.chatbot_conversas import perguntas, despedida, negativas, vaga_inexistente
from entities.models import Vaga

chat_bp = Blueprint('chat', __name__, url_prefix='/gupy')


def check_job_id(job_id):
    vaga = Vaga.query.filter_by(job_id=job_id).first()
    if not vaga:
        return False
    if vaga:
        return True


@chat_bp.route('/get_job_messages', methods=['POST'])
def get_job_messages():
    data = request.get_json()
    user = data['user'].lower()

    if user in negativas:
        session.clear() # encerra a sessão
        return jsonify({'chatbot_resposta': despedida[0]})

    pergunta_atual = session.get('pergunta_atual')
    if pergunta_atual is None and user:
        # se não há uma pergunta atual na sessão, começa do início
        pergunta_atual = 0

    if pergunta_atual == 1:
        if check_job_id(user) == False:
            session.clear() # encerra a sessão
            return jsonify({'chatbot_resposta': vaga_inexistente[0]})

    # verifica se todas as perguntas foram exibidas
    if pergunta_atual >= len(perguntas):
        return jsonify({'chatbot_resposta': 'Não há mais perguntas disponíveis'})

    # recupera a próxima pergunta
    pergunta = perguntas[pergunta_atual]

    # atualiza a pergunta atual na sessão
    session['pergunta_atual'] = pergunta_atual + 1

    return jsonify({'chatbot_resposta': pergunta}), 200
