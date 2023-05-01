from database.database import db
from entities.candidato import Candidato


# insere as informações do candidato no banco de dados
def job_application(nome, email, formacao, tecnologias, job_id):
    try:
        candidato_inscricao = Candidato(nome=nome, email=email, formacao=formacao, tecnologias=tecnologias,
                                        job_id=job_id)
        db.session.add(candidato_inscricao)
        db.session.commit()
    except Exception:
        raise ValueError("Erro ao inserir informações no banco de dados.")
