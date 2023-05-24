import sys
import os

# Obtém o diretório pai do diretório atual (onde o arquivo app.py está localizado)
current_dir = os.path.dirname(os.path.abspath(__file__))

# Obtém o diretório raiz do projeto (pasta 'chatbot_sidi')
project_dir = os.path.dirname(current_dir)

# Adiciona o diretório raiz do projeto ao caminho de importação
sys.path.append(project_dir)

from flask import Flask

from servico_candidato.controllers import candidato_controller
from servico_candidato.database.database import db

app_candidato = Flask(__name__)
app_candidato.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///candidatos.db'
app_candidato.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app_candidato)

# Cria a tabela no banco de dados
with app_candidato.app_context():
    #db.drop_all()
    db.create_all()

# Registra as rotas das vagas
app_candidato.register_blueprint(candidato_controller.candidato_bp)

if __name__ == '__main__':
    app_candidato.run(port=5001)
