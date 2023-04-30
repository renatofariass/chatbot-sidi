from flask import Blueprint, jsonify, request, session

from chatbot.chatbot_conversas import perguntas_python, despedida_eliminado, confirmacao_positiva, respostas_aceitas, \
    desistencia, inscricao_feita, vaga_nao_encontrada
from database.database import db
from entities.candidato import Candidato
from entities.vaga import Vaga
from services.chatbot_service import check_job_id

chat_bp = Blueprint('chat', __name__, url_prefix='/gupy')


@chat_bp.route('/get_job_messages', methods=['POST'])
def get_job_messages():
    # variaveis globais
    global nome, email, formacao, tecnologias, job_id, pergunta

    # atribui o json recebido na requisição a variável data
    data = request.get_json()

    # pega o valor do json com a chave "candidato"
    candidato_resposta = data['candidato'].lower()


    """
    inicia uma sessão, para armazenar o estado do fluxo da conversa, ou seja, se o usuario não for eliminado,
    vai iterando a lista até a última pergunta.
    """
    pergunta_atual = session.get('pergunta_atual', 'boas vindas')
    pergunta = perguntas_python[pergunta_atual]

    """
    Verifica se a pergunta precisa de uma resposta específica para continuar (eliminatória)
    """
    if pergunta_atual in respostas_aceitas and candidato_resposta not in respostas_aceitas[pergunta_atual]:
        session.clear()  # encerra a sessão
        return jsonify({'chatbot': despedida_eliminado['texto']})

    """
    Verifica se a vaga existe no banco de dados
    """
    if pergunta_atual == 'codigo da vaga' and check_job_id(candidato_resposta) is False:
        session.clear()
        return jsonify(
            {'chatbot': vaga_nao_encontrada['texto']}), 404

    if pergunta_atual == 'codigo da vaga' and check_job_id(candidato_resposta) is True:
        session['job_id'] = candidato_resposta
        job_id = session.get('job_id')

    """
    Faz as perguntas pessoais e salva no banco de dados.
    """
    if pergunta_atual == 'nome':
        session['nome'] = str(candidato_resposta).title()  # cria uma sessão nome e atribui a ela a resposta do candidato
        nome = session.get('nome')

    if pergunta_atual == 'email':
        session['email'] = candidato_resposta
        email = session.get('email')

    if pergunta_atual == 'formacao':
        session['formacao'] = str(candidato_resposta).title()
        formacao = session.get('formacao')

    if pergunta_atual == 'tecnologias':
        session['tecnologias'] = candidato_resposta
        tecnologias = session.get('tecnologias')

    """
    verifica se o candidato quer seguir com a candidatura ou não
    """
    if pergunta_atual == 'aviso' and candidato_resposta not in confirmacao_positiva[pergunta_atual]:
        session.clear()  # encerra a sessão
        return jsonify({'chatbot': desistencia['texto']}), 200

    if pergunta_atual == 'aviso' and candidato_resposta in confirmacao_positiva[pergunta_atual]:
        candidato_inscricao = Candidato(nome=nome, email=email, formacao=formacao, tecnologias=tecnologias,
                                        job_id=job_id)
        db.session.add(candidato_inscricao)
        db.session.commit()
        session.clear()  # encerra a sessão
        return jsonify(
            {'chatbot': inscricao_feita['texto']}), 200

    # Avança para a próxima pergunta
    session['pergunta_atual'] = list(perguntas_python.keys())[list(perguntas_python.keys()).index(pergunta_atual) + 1]

    return jsonify({'chatbot': pergunta}), 200
