import random
import re

import requests
from flask import Blueprint, jsonify, request

from chatbot.chatbot import padroes
from services.candidato_service import job_application

chat_bp = Blueprint('chat', __name__, url_prefix='/chatbot')

perguntas = []
indice_pergunta = 0
respostas = {}
job_id = ''


def obter_perguntas(job_id):
    global perguntas

    endpoint_url = f'http://127.0.0.1:5000/perguntas/vaga/{job_id}'
    response = requests.get(endpoint_url)

    if response.status_code == 200:
        data = response.json()
        perguntas = [item['pergunta'] for item in data]
        return True
    else:
        return False


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
        if not obter_perguntas(job_id):
            resposta_personalizada = "Infelizmente, não entendi o que você quis dizer. Pode ser que seu código de " \
                                     "vaga esteja inválido ou eu ainda não fui programado para entender essas palavras. " \
                                     "Tente novamente."
            return jsonify({'chatbot': resposta_personalizada}), 400

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
        salvar_respostas(respostas, job_id)
        indice_pergunta = 0
        respostas = {}
        perguntas = []
        return jsonify({'chatbot': 'Sua candidatura a vaga foi registrada com sucesso. Obrigado por participar. :D'})

    pergunta_seguinte = perguntas[indice_pergunta]
    return jsonify({'chatbot': pergunta_seguinte})


def salvar_respostas(respostas, job_id):
    # Função para salvar as respostas no banco de dados ou fazer o processamento necessário
    nome = respostas.get('Qual seu nome?')
    email = respostas.get('Qual é o seu email?')
    formacao = respostas.get('Qual sua formação?')
    tecnologias = respostas.get('Fale sobre quais tecnologias você possui conhecimentos.')

    # Faça o processamento necessário com as respostas (por exemplo, salvar no banco de dados)
    try:
        job_application(nome, email, formacao, tecnologias, job_id)
    except Exception as e:
        return jsonify({'mensagem': str(e)}), 500


def questao_eliminatoria(job_id, pergunta):
    # Função para verificar se a pergunta é classificada como eliminatória
    endpoint_url = f'http://127.0.0.1:5000/perguntas/vaga/{job_id}'
    response = requests.get(endpoint_url)

    if response.status_code == 200:
        data = response.json()
        for item in data:
            if item['pergunta'] == pergunta and item.get('eliminatoria') is True:
                return True

    return False
