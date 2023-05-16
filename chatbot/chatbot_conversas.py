from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

from entities.pergunta import Pergunta


class ChatBotConfig:
    def __init__(self):
        self.chatbot = ChatBot('MeuChatBot')
        self.trainer = ListTrainer(self.chatbot)

    def treinar_chatbot_com_perguntas_do_banco(self):
        # Recuperar as perguntas do banco de dados
        perguntas = Pergunta.query.all()

        # Treinar o chatbot com as perguntas
        for pergunta in perguntas:
            self.trainer.train([pergunta.pergunta])

    def obter_resposta(self, pergunta):
        # Obter a resposta do chatbot para uma pergunta
        resposta = self.chatbot.get_response(pergunta).text
        return resposta


chatbot_config = ChatBotConfig()
chatbot_config.treinar_chatbot_com_perguntas_do_banco()
