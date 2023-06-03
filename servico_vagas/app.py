import sys
import os

# Obtém o diretório pai do diretório atual (onde o arquivo app.py está localizado)
current_dir = os.path.dirname(os.path.abspath(__file__))

# Obtém o diretório raiz do projeto (pasta 'chatbot_sidi')
project_dir = os.path.dirname(current_dir)

# Adiciona o diretório raiz do projeto ao caminho de importação
sys.path.append(project_dir)

from flask import Flask

from servico_vagas.controllers import vaga_controller, pergunta_controller
from servico_vagas.database.database import db

app = Flask(__name__)
app.secret_key = 'teste'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vagas.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Cria a tabela no banco de dados
with app.app_context():
    #db.drop_all()
    db.create_all()

# Registra as rotas das vagas
app.register_blueprint(vaga_controller.vagas_bp)
app.register_blueprint(pergunta_controller.perguntas_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
