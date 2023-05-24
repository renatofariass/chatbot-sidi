import random
import re

from flask import Blueprint, jsonify, request

from servico_chatbot.chatbot.chatbot import padroes
from servico_chatbot.services.chatbot_service import inscricao_candidato, obter_perguntas, questao_eliminatoria

chat_bp = Blueprint('chat', __name__, url_prefix='/chatbot')

perguntas = []
indice_pergunta = 0
respostas = {}
job_id = ''


@chat_bp.route('', methods=['POST'])
def chatbot_endpoint():
    global perguntas
    global indice_pergunta
    global respostas
    global job_id

    candidato = request.get_json()
    resposta_candidato = candidato.get('resposta')
    resposta_candidato = resposta_candidato.lower()

    for padrao, respostas_padrao in padroes:
        if re.match(padrao, resposta_candidato):
            nltk_resposta = random.choice(respostas_padrao)
            return jsonify({'chatbot': nltk_resposta})

    if not perguntas:
        if resposta_candidato is not None:
            job_id = resposta_candidato  # Salva a resposta da primeira pergunta como job_id
        success, perguntas = obter_perguntas(job_id)
        if not success:
            resposta_personalizada = "Infelizmente, não entendi o que você quis dizer. Pode ser que seu código de " \
                                     "vaga esteja inválido ou eu ainda não fui programado para entender essas palavras. " \
                                     "Tente novamente."
            return jsonify({'chatbot': resposta_personalizada})

    if resposta_candidato == '0':
        indice_pergunta = 0
        respostas = {}
        perguntas = []
        return jsonify({'chatbot': 'Esse conhecimento é obrigatório para essa vaga. Tente outras vagas disponíveis!'})

    pergunta_atual = perguntas[indice_pergunta]

    # Verifica se a pergunta atual é eliminatória
    if questao_eliminatoria(job_id, pergunta_atual):
        if resposta_candidato not in ['0', '1']:
            indice_pergunta = 0
            return jsonify({'chatbot': pergunta_atual})

    pergunta_atual_anterior = perguntas[indice_pergunta]  # Armazena a pergunta atual antes de atualizar o índice
    respostas[pergunta_atual_anterior] = resposta_candidato
    indice_pergunta += 1

    if indice_pergunta >= len(perguntas):
        inscricao_candidato(respostas, job_id)
        indice_pergunta = 0
        respostas = {}
        perguntas = []
        return jsonify({'chatbot': 'Sua candidatura a vaga foi registrada com sucesso. Obrigado por participar. :D'})

    pergunta_seguinte = perguntas[indice_pergunta]
    return jsonify({'chatbot': pergunta_seguinte})
