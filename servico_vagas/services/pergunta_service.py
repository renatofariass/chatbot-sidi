from servico_vagas.database.database import db
from servico_vagas.entities.pergunta import Pergunta
from servico_vagas.entities.vaga import Vaga


def create_pergunta(pergunta, eliminatoria, job_id):
    try:
        vaga = Vaga.query.filter_by(job_id=job_id).first()
        if not vaga:
            raise ValueError("A vaga com o job_id '{}' não existe.".format(job_id))
        nova_pergunta = Pergunta(pergunta=pergunta, eliminatoria=eliminatoria, vaga=vaga)
        db.session.add(nova_pergunta)
        db.session.commit()
    except Exception:
        raise ValueError("Erro ao criar pergunta. Id da vaga não existe.")


def listar_perguntas(job_id):
    try:
        vaga = Vaga.query.filter_by(job_id=job_id).first()
        if not vaga:
            raise ValueError("job_id '{}' não encontrado.".format(job_id))

        perguntas = [pergunta.to_dict() for pergunta in vaga.perguntas]

        return perguntas
    except Exception:
        raise ValueError("Erro ao buscar vaga com job_id '{}'.".format(job_id))
