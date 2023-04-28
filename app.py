from flask import Flask

from controllers import bot_controller, vaga_controller
from database.database import db

app = Flask(__name__)
app.secret_key = 'teste'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vagas.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Cria a tabela no banco de dados
with app.app_context():
    """try:
        db.drop_all()
    except:
        pass"""
    # Cria as tabelas novamente
    db.create_all()

# Registra as rotas das vagas
app.register_blueprint(vaga_controller.vagas_bp)
app.register_blueprint(bot_controller.chat_bp)

if __name__ == '__main__':
    app.run()
