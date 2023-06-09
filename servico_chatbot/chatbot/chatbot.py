from nltk.chat import Chat
from nltk.chat.util import reflections

padroes = [
    (r"!menu|!!menu",
     ["Comandos que você pode usar: \n !saber - Saber mais sobre o Chatbot SiDi. \n !sidi - Redes sociais da SiDi. \n"
      "!pergunta - Prosseguir para as perguntas da vaga. \n !ajuda - Como navegar pelo Chatbot SiDi. \n !vaga - Vagas disponíveis aqui na SiDi. \n "
      "!sair - Encerrar a sessão."]),
    
    (r"!vaga|!vagas|!!vaga|!!vagas",
     ["Encontre a vaga que mais combina com o seu perfil. 🎯 \n Vagas disponíveis: https://sidi.gupy.io/"]),

    (r"!saber|!!saber",
     ["!serve - Para que o Chatbot SiDi serve? \n !funciona - Como funciona o ChatBot SiDi?"]),

    (r"!ajuda|!!ajuda",
     ["Eu funciono através de comandos começados com '!'. Então para todos os comandos que quiser que eu execute coloque o '!' na frente da palavra."]),
    
    (r"!sidi|!!sidi|!instagram|!linkedin|!facebook|!linktree|!redes",
     ["Siga a gente nas redes sociais para ficar por dentro das vagas. 🥰 \n "
      "LinkedIn: https://www.linkedin.com/company/segueosidi \n "
      "Instagram: https://www.instagram.com/segueosidi \n "
      "Facebook: https://www.facebook.com/segueosidi \n "
      "Linktree: https://linktr.ee/segueosidi"]),

    (r"!perguntas|!pergunta|!!pergunta|!!perguntas", ["Ok, você quer ir para as perguntas. Por favor, informe o seu código de vaga. Ex. 123"]),

    (r"!serve|!!serve", [
        "Eu ajudo no recrutamento de candidatos, avaliando se os candidatos estão aptos para as "
        "vagas ou não, com base nas perguntas que meus criadores disponibilizaram para as vagas."]),

    (r"!funciona|!!funciona", [
        "Eu faço perguntas aos candidatos com base na vaga relacionada e se o candidato passar pela triagem das "
        "perguntas, eu salvo a inscrição dele no meu banco de dados."]),

    (r"(.*)seu nome(.*)|(.*)teu nome(.*)", ["Meu nome é ChatBot Sidi"]),

    (r"(.*)(candidatar|inscrição)(.*)", ["Por favor, informe o seu código de vaga para prosseguir. Ex. 123"]),

    (r"(!sair|!sai)", ["Tchau, tchau! 👋🙂"])
]

chatbot = Chat(padroes, reflections)
