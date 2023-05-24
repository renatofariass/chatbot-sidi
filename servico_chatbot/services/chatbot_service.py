import requests


# Função para verificar se a pergunta é classificada como eliminatória
def questao_eliminatoria(job_id, pergunta):
    obter_perguntas_url = f'http://127.0.0.1:5000/perguntas/vaga/{job_id}'
    response = requests.get(obter_perguntas_url)

    if response.status_code == 200:
        data = response.json()
        for item in data:
            if item['pergunta'] == pergunta and item.get('eliminatoria') is True:
                return True

    return False


def obter_perguntas(job_id):
    obter_perguntas_url = f'http://127.0.0.1:5000/perguntas/vaga/{job_id}'

    try:
        response = requests.get(obter_perguntas_url)
        if response.status_code == 200:
            data = response.json()
            perguntas = [item['pergunta'] for item in data]
            return perguntas
        else:
            return False
    except requests.exceptions.RequestException:
        return False


def inscricao_candidato(respostas, job_id):
    criar_candidato_url = 'http://127.0.0.1:5001/candidato/create'
    data = {
        'respostas': respostas,
        'job_id': job_id
    }

    try:
        response = requests.post(criar_candidato_url, json=data)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.RequestException:
        return False
