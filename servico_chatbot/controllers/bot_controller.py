import random
import re

from flask import Blueprint, jsonify, request

from servico_chatbot.chatbot.chatbot import padroes
from servico_chatbot.services.chatbot_service import (
    inscricao_candidato,
    obter_perguntas,
    questao_eliminatoria,
)

chat_bp = Blueprint("chat", __name__, url_prefix="/chatbot")

perguntas = []
indice_pergunta = 0
contador = 0
contador_eliminatoria = 0
respostas = {}
job_id = ""


@chat_bp.route("", methods=["OPTIONS"])
def handle_options_request():
    # Configurar e retornar os cabeçalhos de resposta adequados para o CORS
    response_headers = {
        "Access-Control-Allow-Origin": "http://localhost:3000",
        "Access-Control-Allow-Methods": "POST",
        "Access-Control-Allow-Headers": "Content-Type",
    }
    return ("", 204, response_headers)


@chat_bp.route("", methods=["POST"])
def chatbot_endpoint():
    global perguntas
    global indice_pergunta
    global respostas
    global job_id
    global contador
    global contador_eliminatoria

    candidato = request.get_json()
    resposta_candidato = candidato.get("resposta")
    resposta_candidato = resposta_candidato.lower()

    for padrao, respostas_padrao in padroes:
        if re.match(padrao, resposta_candidato):
            indice_pergunta = 0
            contador = 0
            contador_eliminatoria = 0
            respostas.clear()
            perguntas = []
            nltk_resposta = random.choice(respostas_padrao)
            return jsonify({"chatbot": nltk_resposta})

    if not perguntas:
        if resposta_candidato is not None:
            job_id = (
                resposta_candidato  # Salva a resposta da primeira pergunta como job_id
            )
            if any(char.isdigit() for char in resposta_candidato):
                try:
                    perguntas = obter_perguntas(job_id)
                    if not perguntas:
                        resposta_personalizada = "Você informou um código de vaga inválido. Fale com um dos nossos recrutadores e tente novamente. 😕"
                        return jsonify({"chatbot": resposta_personalizada})
                except Exception as e:
                    resposta_personalizada = "Ocorreu um erro ao obter as perguntas 😕. Tente novamente mais tarde."
                    return jsonify({"chatbot": resposta_personalizada})
            else:
                resposta_personalizada = "Desculpe, não estou programado para entender o que você digitou. Use os comandos indicados, por favor. 😕"
                return jsonify({"chatbot": resposta_personalizada})

    # atualiza a pergunta atual
    pergunta_atual = perguntas[indice_pergunta]

    # Verifica se a pergunta atual é eliminatória
    eliminatoria = questao_eliminatoria(job_id, pergunta_atual)

    if (
        eliminatoria is False
        and indice_pergunta == 0
        and resposta_candidato in [job_id, "0", "1"]
    ):
        indice_pergunta = 0
        if contador == 0:
            contador += 1
            contador_eliminatoria += 1
            return jsonify({"chatbot": pergunta_atual})
        
        if contador == 1:
            contador += 1
            return jsonify({"chatbot": "Forneça uma resposta válida. 🤨"})
        
        if contador == 2:
            indice_pergunta = 0
            contador_eliminatoria = 0
            contador = 0
            respostas.clear()
            perguntas.clear()
            return jsonify(
                {"chatbot": "Você foi desclassificado por muitas tentativas erradas. 😕"}
            )

    if eliminatoria is True:
        if indice_pergunta >= (int(len(perguntas)) - 1) and resposta_candidato == "0":
            indice_pergunta = 0
            contador_eliminatoria = 0
            contador = 0
            respostas.clear()
            perguntas.clear()
            return jsonify({"chatbot": "Sua candidatura foi cancelada. 😕"})

        if resposta_candidato not in ["0", "1"]:
            if contador_eliminatoria == 0:
                contador_eliminatoria += 1
                return jsonify({"chatbot": pergunta_atual})

            if contador_eliminatoria == 1:
                contador_eliminatoria += 1
                return jsonify({"chatbot": "Digite 0 ou 1, por favor."})

            if contador_eliminatoria == 2:
                indice_pergunta = 0
                respostas.clear()
                perguntas.clear()
                contador_eliminatoria = 0
                contador = 0
                return jsonify(
                    {
                        "chatbot": "Você foi desclassificado por muitas tentativas erradas. 😕"
                    }
                )

        if resposta_candidato == "0":
            indice_pergunta = 0
            contador_eliminatoria = 0
            contador = 0
            respostas.clear()
            perguntas.clear()
            return jsonify(
                {
                    "chatbot": "Infelizmente, esse requisito é obrigatório para essa vaga 😕. Tente outras vagas disponíveis! 👇 \n " +
                    "Vagas disponíveis: https://sidi.gupy.io/"
                }
            )

    pergunta_anterior = perguntas[indice_pergunta]  # Armazena a pergunta atual antes de atualizar o índice
    respostas[pergunta_anterior] = resposta_candidato  # salva a resposta do candidato pra cada pergunta
    indice_pergunta += 1  # atualiza o indice de pergunta

    if indice_pergunta >= len(perguntas):
        try:
            inscricao = inscricao_candidato(respostas, job_id)
            if inscricao is True:
                indice_pergunta = 0
                contador = 0
                contador_eliminatoria = 0
                respostas.clear()
                perguntas.clear()
                return jsonify(
                    {
                        "chatbot": "Sua candidatura a vaga foi registrada com sucesso. Obrigado por participar. Boa sorte! 👋😃"
                    }
                )
            else:
                indice_pergunta = 0
                contador = 0
                contador_eliminatoria = 0
                respostas.clear()
                perguntas.clear()
                return jsonify({"chatbot": "Você já se candidatou nessa vaga. Tente outras. 🧐"})
            
        except Exception:
            indice_pergunta = 0
            contador = 0
            contador_eliminatoria = 0
            respostas.clear()
            perguntas.clear()
            return jsonify(
                {
                    "chatbot": "Ocorreu um erro ao salvar sua candidatura. Tente novamente mais tarde. 😕"
                }
            )

    pergunta_seguinte = perguntas[indice_pergunta]
    return jsonify({"chatbot": pergunta_seguinte})
