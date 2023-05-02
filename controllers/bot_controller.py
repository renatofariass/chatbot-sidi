from flask import Blueprint, jsonify, request, session

from chatbot.chatbot_conversas import perguntas_python, despedida_eliminado, confirmacao_positiva, respostas_aceitas, \
    desistencia, inscricao_feita, vaga_nao_encontrada
from services.candidato_service import job_application
from services.vaga_service import check_job_id

chat_bp = Blueprint('chat', __name__, url_prefix='/gupy')

# fluxo de mensagens do chatbot
@chat_bp.route('/get_job_messages', methods=['POST'])
def get_job_messages():
    global nome, email, formacao, tecnologias, job_id, pergunta

    # atribui o json recebido na requisição a variável data
    data = request.get_json()

    # pega o valor do json com a chave "candidato"
    candidato_resposta = data['candidato'].lower()

    """
    inicia uma sessão para manter o fluxo de conversa e iterar a lista de perguntas até a última pergunta.
    """
    pergunta_atual = session.get('pergunta_atual', 'boas vindas')  # começa com a pergunta "boas vindas"
    pergunta = perguntas_python[pergunta_atual]

    """
    Verifica se a pergunta atual precisa de uma resposta "sim" para continuar (eliminatória)
    """
    if pergunta_atual in respostas_aceitas and candidato_resposta not in respostas_aceitas[pergunta_atual]:
        session.clear()  # encerra a sessão
        return jsonify({'chatbot': despedida_eliminado['texto']})

    """
    Verifica se a vaga existe no banco de dados, caso exista, avança para a próxima pergunta.
    """
    if pergunta_atual == 'codigo da vaga' and check_job_id(candidato_resposta) is False:
        session.clear()
        return jsonify({'chatbot': vaga_nao_encontrada['texto']}), 404

    if pergunta_atual == 'codigo da vaga' and check_job_id(candidato_resposta) is True:
        # armazena a resposta do código da vaga informada pelo candidato em uma sessão
        session['job_id'] = candidato_resposta
        job_id = session.get('job_id')

    """
    Caso as perguntas estejam nas perguntas pessoais, salva as respostas do candidato em uma variável para 
    posteriormente ser inseridas no banco de dados.
    """
    if pergunta_atual == 'nome':
        session['nome'] = str(candidato_resposta).title()
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
    verifica se o candidato quer seguir com a candidatura ou não, caso não a sessao é encerrada e caso sim insere as
    informações do candidato no banco de dados
    """
    if pergunta_atual == 'aviso' and candidato_resposta not in confirmacao_positiva[pergunta_atual]:
        session.clear()
        return jsonify({'chatbot': desistencia['texto']}), 200

    if pergunta_atual == 'aviso' and candidato_resposta in confirmacao_positiva[pergunta_atual]:
        try:
            job_application(nome, email, formacao, tecnologias, job_id)  # insere informaçoes no banco de dados
            session.clear()
            return jsonify(
                {'chatbot': inscricao_feita['texto']}), 200
        except Exception as e:
            error_msg = {'mensagem': '{}'.format(str(e))}
            return jsonify(error_msg), 500

    # Avança para a próxima pergunta
    session['pergunta_atual'] = list(perguntas_python.keys())[list(perguntas_python.keys()).index(pergunta_atual) + 1]

    return jsonify({'chatbot': pergunta}), 200
