from sqlalchemy.exc import IntegrityError

from servico_vagas.database.database import db
from servico_vagas.entities.vaga import Vaga


# cria uma vaga
def create_vaga(job_id, descricao_vaga, nivel_vaga):
    try:
        vaga = Vaga(job_id=job_id, descricao_vaga=descricao_vaga, nivel_vaga=nivel_vaga)
        db.session.add(vaga)
        db.session.commit()
    except IntegrityError:
        raise ValueError("O job_id '{}' já está em uso.".format(job_id))
    except Exception:
        raise ValueError("Erro ao criar vaga.")


# busca uma vaga pelo job_id e retorna true caso exista
def check_job_id(id):
    try:
        vaga = Vaga.query.filter_by(job_id=id).first()
        return vaga.to_dict()
    except Exception:
        raise ValueError("job_id '{}' não encontrado.".format(id))


# busca todas as vagas
def listar_vagas():
    vagas = Vaga.query.all()
    # transforma as vagas para o formato json
    vagas_dict = [vaga.to_dict() for vaga in vagas]
    return list(vagas_dict)
