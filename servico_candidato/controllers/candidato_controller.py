from flask import Blueprint, jsonify, request

from servico_candidato.services.candidato_service import job_application

candidato_bp = Blueprint('chat', __name__, url_prefix='/candidato')

# pega as respostas dos dados do candidato que ele passou no chatbot e salva no banco de dados
@candidato_bp.route('/create', methods=['POST'])
def salvar_respostas():
    candidato = request.get_json()
    respostas = candidato.get('respostas')
    job_id = candidato.get('job_id')

    nome = respostas.get('Qual seu nome?')
    email = respostas.get('Qual é o seu email?')
    linkedin = respostas.get('Qual o seu linkedin?')
    github = respostas.get('Qual o seu github?')
    formacao = respostas.get('Qual sua formação?')
    tecnologias = respostas.get('Fale sobre quais tecnologias você possui conhecimentos.')

    try:
        job_application(nome=nome, email=email, linkedin=linkedin, github=github, formacao=formacao,
                        tecnologias=tecnologias, job_id=job_id)
        return jsonify({'mensagem': 'Respostas salvas com sucesso.'}), 200
    except Exception as e:
        return jsonify({'mensagem': str(e)}), 500