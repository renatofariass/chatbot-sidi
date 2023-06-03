import sys
import os

# Obtém o diretório pai do diretório atual (onde o arquivo app.py está localizado)
current_dir = os.path.dirname(os.path.abspath(__file__))

# Obtém o diretório raiz do projeto (pasta 'chatbot_sidi')
project_dir = os.path.dirname(current_dir)

# Adiciona o diretório raiz do projeto ao caminho de importação
sys.path.append(project_dir)

from flask import Flask
from servico_chatbot.controllers import bot_controller
from flask_cors import CORS


app_chatbot = Flask(__name__)
CORS(app_chatbot, origins=['http://localhost:3000'])

# Registra as rotas das vagas
app_chatbot.register_blueprint(bot_controller.chat_bp)


if __name__ == '__main__':
    app_chatbot.run(host='0.0.0.0', port=5002)
