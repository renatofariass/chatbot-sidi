from servico_candidato.database.database import db

class Candidato(db.Model):
    __tablename__ = 'candidatos'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    linkedin = db.Column(db.String(255), nullable=False)
    github = db.Column(db.String(255), nullable=False)
    formacao = db.Column(db.String(255), nullable=False)
    tecnologias = db.Column(db.String(255), nullable=False)
    job_id = db.Column(db.String(255), nullable=False)

    def to_dict(self):
        return {'nome': self.nome, 'email': self.email, 'linkedin': self.linkedin, 'github': self.github,
                'formacao': self.formacao, 'tecnologias': self.tecnologias}