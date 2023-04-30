from database.database import db


class Vaga(db.Model):
    __tablename__ = 'vagas'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    job_id = db.Column(db.String(50), nullable=False, unique=True)
    descricao_vaga = db.Column(db.String(255), nullable=False)
    nivel_vaga = db.Column(db.String(20), nullable=False)

    def to_dict(self):
        return {'job_id': self.job_id, 'descricao_vaga': self.descricao_vaga, 'nivel_vaga': self.nivel_vaga}
