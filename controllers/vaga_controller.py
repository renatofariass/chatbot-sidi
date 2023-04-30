import json

from flask import Blueprint, Response, request

from database.database import db
from entities.vaga import Vaga

vagas_bp = Blueprint('vagas', __name__, url_prefix='/vagas')


# Lista todas as vagas
@vagas_bp.route('', methods=['GET'])
def listar_vagas():
    vagas = Vaga.query.all()
    vagas_dict = [vaga.to_dict() for vaga in vagas]
    vagas_json = json.dumps(vagas_dict, separators=(',', ':'))
    response = Response(vagas_json, status=200, mimetype='application/json')
    return response


# Cria uma nova vaga
@vagas_bp.route('', methods=['POST'])
def criar_vaga():
    job_id = request.json['job_id']
    descricao_vaga = request.json['descricao_vaga']
    nivel_vaga = request.json['nivel_vaga']
    vaga = Vaga(job_id=job_id, descricao_vaga=descricao_vaga, nivel_vaga=nivel_vaga)
    db.session.add(vaga)
    db.session.commit()
    vaga_json = json.dumps(vaga.to_dict(), separators=(',', ':'))
    response = Response(vaga_json, status=201, mimetype='application/json')
    return response
