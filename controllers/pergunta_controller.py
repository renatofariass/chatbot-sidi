from flask import Blueprint, request, jsonify

from services.pergunta_service import create_pergunta, listar_perguntas

perguntas_bp = Blueprint('perguntas', __name__, url_prefix='/perguntas')


@perguntas_bp.route('/create/<string:job_id>', methods=['POST'])
def create(job_id):
    pergunta = request.json['pergunta']
    create_pergunta(pergunta = pergunta, job_id = job_id)
    return jsonify({'mensagem': 'Pergunta criada com sucesso!'}), 201


@perguntas_bp.route('/vaga/<string:job_id>', methods=['GET'])
def find_perguntas(job_id):
    try:
        return listar_perguntas(job_id)
    except Exception as e:
        return jsonify({'mensagem': str(e)}), 500