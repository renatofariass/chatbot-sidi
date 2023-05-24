import requests


# Função para verificar se a pergunta é classificada como eliminatória
def questao_eliminatoria(job_id, pergunta):
    endpoint_url = f'http://127.0.0.1:5000/perguntas/vaga/{job_id}'
    response = requests.get(endpoint_url)

    if response.status_code == 200:
        data = response.json()
        for item in data:
            if item['pergunta'] == pergunta and item.get('eliminatoria') is True:
                return True

    return False


def obter_perguntas(job_id):
    endpoint_url = f'http://127.0.0.1:5000/perguntas/vaga/{job_id}'

    try:
        response = requests.get(endpoint_url)
        if response.status_code == 200:
            data = response.json()
            perguntas = [item['pergunta'] for item in data]
            return True, perguntas
        else:
            return False, 'Ocorreu um erro ao obter as perguntas. Tente novamente.'
    except requests.exceptions.RequestException:
        return False, 'Ocorreu um erro ao conectar com o serviço de perguntas. Tente novamente.'


def inscricao_candidato(respostas, job_id):
    candidato_service_url = 'http://127.0.0.1:5001/candidato/create'
    data = {
        'respostas': respostas,
        'job_id': job_id
    }

    try:
        response = requests.post(candidato_service_url, json=data)
        if response.status_code == 200:
            return True, 'Sua candidatura a vaga foi registrada com sucesso. Boa sorte e obrigado por participar!! :D'
        else:
            return False, 'Ocorreu um erro ao registrar sua candidatura. Tente novamente.'
    except requests.exceptions.RequestException:
        return False, 'Ocorreu um erro ao conectar com o serviço de candidato. Tente novamente.'
