from nltk.chat import Chat
from nltk.chat.util import reflections

padroes = [
    (r"olá!|oi|olá|ola|ola!|voltar|menu",
     ["Olá, seja bem vindo ao Chatbot SiDi. O que você quer fazer? opcao_a - Saiba mais sobre o Chatbot SiDi opcao_b "
      "- Prosseguir para as perguntas"]),

    (r"opcao_a", ["1a - Para que o chatbot SiDi serve? 2a - Como funciona o ChatBot SiDi? b - Prosseguir para as "
                  "perguntas"]),

    (r"1a", [
        "Eu ajudo no recrutamento de candidatos, avaliando se os candidatos estão aptos para as "
        "vagas ou não, com base nos parâmetros que meus criadores passaram."]),

    (r"2a", [
        "Eu faço perguntas aos candidatos com base na vaga relacionada e se o usuário passar pela triagem das "
        "perguntas, eu salvo a inscrição dele no meu banco de dados."]),

    (r"opcao_b", ["Por favor, informe o seu código de vaga."]),

    (r"qual é o seu nome?", ["Meu nome é ChatBot Sidi"]),
    (r"como você está?|como voce esta?|como vai?", ["Estou bem, obrigado!", "Vou bem, obrigado!"]),
    (r"(.*)(candidatar|inscrição|vaga)(.*)", ["Por favor, informe o seu código de vaga para prosseguir."])
]

chatbot = Chat(padroes, reflections)
