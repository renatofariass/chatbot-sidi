import json

from flask import Blueprint, Response, request, jsonify

from database.database import db
from entities.vaga import Vaga
from services.vaga_service import create_vaga, listar_vagas

vagas_bp = Blueprint('vagas', __name__, url_prefix='/vagas')


# Lista todas as vagas
@vagas_bp.route('', methods=['GET'])
def find_all():
    vagas_json = json.dumps(listar_vagas(), separators=(',', ':'))
    response = Response(vagas_json, status=200, mimetype='application/json')
    return response

# criar vagas
@vagas_bp.route('/create', methods=['POST'])
def create():
    try:
        job_id = request.json['job_id']
        descricao_vaga = request.json['descricao_vaga']
        nivel_vaga = request.json['nivel_vaga']
        create_vaga(job_id, descricao_vaga, nivel_vaga)
        return jsonify({'mensagem': 'Vaga criada com sucesso!'}), 200
    except Exception as e:
        error_msg = {'mensagem': 'Erro ao criar vaga: {}'.format(str(e))}
        return jsonify(error_msg), 500
