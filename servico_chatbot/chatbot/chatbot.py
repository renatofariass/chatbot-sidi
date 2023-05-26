from nltk.chat import Chat
from nltk.chat.util import reflections

padroes = [
    (r"!menu",
     ["comandos que você pode usar: | !saber - Saber mais sobre o Chatbot SiDi | !sidi - Saber mais sobre a SiDi "
      "| !perguntas - Prosseguir para as perguntas | !ajuda - Como navegar pelo Chatbot SiDi | !redes - Redes Sociais da SiDi"]),

    (r"!saber",
     ["!serve - Para que o Chatbot SiDi serve? | !funciona - Como funciona o ChatBot SiDi? | !perguntas - Prosseguir para as "
         "perguntas | !ajuda - Como navegar pelo Chatbot SiDi"]),

    (r"!ajuda",
     ["Eu funciono através de comandos começados com '!'. quiser voltar para o Menu digite '!menu' e "
      "se quiser seguir para as perguntas digite '!perguntas'"]),
    
    (r"!redes",
     ["Siga a gente nas redes sociais para ficar por dentro das vagas :) | "
      "LinkedIn: https://www.linkedin.com/company/segueosidi/ | "
      "Instagram: https://www.instagram.com/segueosidi/ | "
      "Facebook: https://www.facebook.com/segueosidi"]),

    (r"!sidi",
     ["Ótimo que você queira saber mais sobre a nossa empresa!! Segue o link: https://www.sidi.org.br/sobre-nos/"]),

    (r"!perguntas", ["Ok, você quer ir para as perguntas. Por favor, informe o seu código de vaga. Ex. 123"]),

    (r"!serve", [
        "Eu ajudo no recrutamento de candidatos, avaliando se os candidatos estão aptos para as "
        "vagas ou não, com base nas perguntas que meus criadores disponibilizaram para as vagas."]),

    (r"!funciona", [
        "Eu faço perguntas aos candidatos com base na vaga relacionada e se o candidato passar pela triagem das "
        "perguntas, eu salvo a inscrição dele no meu banco de dados."]),

    (r"(.*)seu nome(.*)|(.*)teu nome(.*)", ["Meu nome é ChatBot Sidi"]),

    (r"(.*)(candidatar|inscrição|vaga)(.*)", ["Por favor, informe o seu código de vaga para prosseguir."]),

    (r"(sair|tchau|até mais|ate mais|até logo|ate logo)", ["Até mais!", "Tchau, tchau!"])
]

chatbot = Chat(padroes, reflections)
