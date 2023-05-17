from flask import Blueprint, request, jsonify

from services.pergunta_service import create_pergunta, listar_perguntas

perguntas_bp = Blueprint('perguntas', __name__, url_prefix='/perguntas')


@perguntas_bp.route('/create/<string:job_id>', methods=['POST'])
def create(job_id):
    try:
        pergunta = request.json['pergunta']
        eliminatoria = request.json['eliminatoria']
        create_pergunta(pergunta=pergunta, eliminatoria=eliminatoria, job_id=job_id)
        return jsonify({'mensagem': 'Pergunta criada com sucesso!'}), 201
    except Exception as e:
        return jsonify({'mensagem': str(e)}), 404



@perguntas_bp.route('/vaga/<string:job_id>', methods=['GET'])
def find_perguntas(job_id):
    try:
        return listar_perguntas(job_id)
    except Exception as e:
        return jsonify({'mensagem': str(e)}), 500