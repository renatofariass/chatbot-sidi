import requests
from chatterbot import ChatBot
from flask import Blueprint, jsonify, request
from services.candidato_service import job_application

chat_bp = Blueprint('chat', __name__, url_prefix='/chatbot')

perguntas = []
indice_pergunta = 0
respostas = {}


def obter_perguntas(job_id):
    global perguntas
    global indice_pergunta

    endpoint_url = f'http://127.0.0.1:5000/perguntas/vaga/{job_id}'
    response = requests.get(endpoint_url)

    if response.status_code == 200:
        data = response.json()
        perguntas = [item['pergunta'] for item in data]
        indice_pergunta = 0
        return True
    else:
        return False


@chat_bp.route('<string:job_id>', methods=['POST'])
def chatbot_endpoint(job_id):
    global perguntas
    global indice_pergunta
    global respostas

    candidato = request.get_json()
    resposta = candidato.get('resposta')

    if not perguntas:
        if not obter_perguntas(job_id):
            return jsonify({'chatbot': 'Erro ao obter perguntas'}), 500

    if resposta == '0':
        indice_pergunta = 0
        respostas.clear()
        return jsonify({'chatbot': 'Desculpe'})

    if indice_pergunta >= len(perguntas):
        salvar_respostas(respostas, job_id)
        return jsonify({'chatbot': 'Fim das perguntas'})

    pergunta_atual = perguntas[indice_pergunta]

    # Verifica se a pergunta atual é eliminatória
    if is_eliminatory_question(job_id, pergunta_atual):
        if resposta not in ['0', '1']:
            return jsonify({'chatbot': 'Por favor, responda com 0 ou 1.' + pergunta_atual})

    respostas[pergunta_atual] = resposta
    indice_pergunta += 1

    return jsonify({'chatbot': perguntas[indice_pergunta - 1]})



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


def is_eliminatory_question(job_id, pergunta):
    # Função para verificar se a pergunta é classificada como eliminatória
    endpoint_url = f'http://127.0.0.1:5000/perguntas/vaga/{job_id}'
    response = requests.get(endpoint_url)

    if response.status_code == 200:
        data = response.json()
        for item in data:
            if item['pergunta'] == pergunta and item.get('eliminatoria') is True:
                return True

    return False

