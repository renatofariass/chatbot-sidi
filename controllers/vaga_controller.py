import json

from flask import Blueprint, Response, request, jsonify

from services.vaga_service import create_vaga, listar_vagas, check_job_id

vagas_bp = Blueprint('vagas', __name__, url_prefix='/vagas')


@vagas_bp.route('/<string:id>', methods=['GET'])
def find_by_id(id):
    try:
        vagas_json = json.dumps(check_job_id(id), separators=(',', ':'))
        response = Response(vagas_json, status=200, mimetype='application/json')
    except Exception as e:
        error_msg = {'mensagem': '{}'.format(str(e))}
        return jsonify(error_msg), 404
    return response


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
