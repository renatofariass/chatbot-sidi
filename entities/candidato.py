from database.database import db


class Candidato(db.Model):
    __tablename__ = 'candidatos'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    formacao = db.Column(db.String(255), nullable=False)
    tecnologias = db.Column(db.String(255), nullable=False)
    job_id = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        return {'nome': self.nome, 'email': self.email, 'formacao': self.formacao, 'tecnologias': self.tecnologias}