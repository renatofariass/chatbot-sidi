from servico_candidato.database.database import db
from servico_candidato.entities.candidato import Candidato


# insere as informações do candidato no banco de dados
def job_application(nome, email, linkedin, github, formacao, tecnologias, job_id):
    try:
        candidato_inscricao = Candidato(nome=nome, email=email, linkedin=linkedin, github=github, formacao=formacao,
                                        tecnologias=tecnologias, job_id=job_id)
        db.session.add(candidato_inscricao)
        db.session.commit()
    except Exception:
        raise ValueError("Erro ao inserir informações no banco de dados.")
