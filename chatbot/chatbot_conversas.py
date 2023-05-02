# perguntas que serão feitas
perguntas_python = {
    'boas vindas': 'Olá, sou o chatbot da SiDi. Seja bem vindo! Informe o código da vaga.',
    'codigo da vaga': "Encontrei a vaga. Você tem experiência na área desejada? Responda com 'Sim' ou 'Não'.",
    'experiencia na area': "Você tem conhecimento do idioma inglês intermediário/avançado? Responda com 'Sim' ou 'Não'.",
    'conhecimento em ingles': "Você tem conhecimento em Python? Responda com 'Sim' ou 'Não'.",
    'conhecimento em Python': 'Qual seu nome?',
    'nome': 'Qual é o seu email?',
    'email': 'Qual sua formação?',
    'formacao': 'Fale sobre quais tecnologias você possui conhecimentos.',
    'tecnologias': "Você quer confirmar a inscrição para essa vaga? Responda com 'Sim' ou 'Não'",
    'aviso': ''
}

# lista das perguntas eliminatórias e suas respectivas respostas que serão aceitas
respostas_aceitas = {
    'experiencia na area': ['sim.', 'sim', 'sim!', 'si', 'sí'],
    'conhecimento em ingles': ['sim.', 'sim', 'sim!', 'si', 'sí'],
    'conhecimento em Python': ['sim.', 'sim', 'sim!', 'si', 'sí'],
}

# confirmação de inscrição
confirmacao_positiva = {
    'aviso': ['sim.', 'sim', 'sim!', 'si', 'sí']
}

# texto para caso o usuário seja eliminado
despedida_eliminado = {
    'texto': 'Esse conhecimento é obrigatório para essa vaga. Tente outras vagas disponíveis.'
}

# texto para caso o usuário não queira fazer a inscrição
desistencia = {
    'texto': 'confirmado sua desistência da vaga.'
}

# texto para caso o usuário confirme a sua inscrição
inscricao_feita = {
    'texto': 'Sua candidatura a vaga foi registrada com sucesso. Obrigado por participar. :D'
}

# texto para vaga não encontrada
vaga_nao_encontrada = {
    'texto': 'Código da vaga não existe. Por favor, verifique e informe novamente.'
}