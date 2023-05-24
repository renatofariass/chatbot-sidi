from servico_vagas.database.database import db


class Pergunta(db.Model):
    __tablename__ = 'perguntas'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pergunta = db.Column(db.String(255), nullable=False)
    eliminatoria = db.Column(db.Boolean, default=False)
    vaga_job_id = db.Column(db.Integer, db.ForeignKey('vagas.job_id'))

    def to_dict(self):
        return {'pergunta': self.pergunta, 'eliminatoria': self.eliminatoria}


