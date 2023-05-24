from nltk.chat import Chat
from nltk.chat.util import reflections

padroes = [
    (r"olá!|ola|oi|ei|eae|eai|menu",
     ["Olá, seja bem vindo ao Chatbot SiDi. O que você quer fazer? opcao_a - Saber mais sobre o Chatbot SiDi | opcao_b "
      "- Saber mais sobre a SiDi | opcao_c - Prosseguir para as perguntas"]),

    (r"opcao_a", ["1a - Para que o chatbot SiDi serve? | 2a - Como funciona o ChatBot SiDi? c - Prosseguir para as "
                  "perguntas"]),

    (r"opcao_b|(.*)saber mais sobre a empre(.*)",
     ["Ótimo que você queira saber mais sobre a nossa empresa!! Segue o link: https://www.sidi.org.br/sobre-nos/"]),

    (r"opcao_c", ["Ok, você quer ir para as perguntas. Por favor, informe o seu código de vaga."]),

    (r"1a", [
        "Eu ajudo no recrutamento de candidatos, avaliando se os candidatos estão aptos para as "
        "vagas ou não, com base nas perguntas que meus criadores disponibilizaram para as vagas."]),

    (r"2a", [
        "Eu faço perguntas aos candidatos com base na vaga relacionada e se o usuário passar pela triagem das "
        "perguntas, eu salvo a inscrição dele no meu banco de dados."]),

    (r"qual é o seu nome?", ["Meu nome é ChatBot Sidi"]),

    (r"como você está?|como voce esta?|como vai?", ["Estou bem, obrigado!", "Vou bem, obrigado!"]),

    (r"(.*)(candidatar|inscrição|vaga)(.*)", ["Por favor, informe o seu código de vaga para prosseguir."]),

    (r"(sair|tchau|até mais|ate mais|até logo|ate logo)", ["Até mais!", "Tchau, tchau!"])
]

chatbot = Chat(padroes, reflections)
