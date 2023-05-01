## Para rodar o projeto

1 - Instale o Python (> 3 version)

2 - Instale o PIP

3 - Instale a VirtualEnv
 - pip install virtualenv

4 - Crie uma virtual env chamada 'venv'
- python virtualenv venv

5 - ative a virtual env


### Virtual ENV (Windows)


``` 
$ virtualenv venv
```
ATIVAR:
```
$ venv/Scripts/activate
```
DESATIVAR:
```
$ deactivate
```

6 - Instale o Flask e o Flask-SQLAlchemy

``` 
pip install -r requeriments.txt
```

# Rotas da aplicação

## vaga_controller

### Criar vagas (/vagas/create) [POST]
<pre>
Cria vagas. Ex. de como criar uma vaga via requisicão post: 
{
    "job_id": 123, 
    "descricao_vaga": "desenvolvedor python", 
    "nivel_vaga": "pleno"
}
</pre>

### Listar todas as vagas (/vagas) [GET]
<pre>
Lista todas as vagas contidas no banco de dados. Ex de retorno:
[
    {
        "job_id": "123",
        "descricao_vaga": "desenvolvedor python",
        "nivel_vaga": "pleno"
    }
]
</pre>

## bot_controller

### chatbot (/gupy/get_job_messages) [POST]
<pre>
Para iniciar a conversa com o chtatbot você precisa mandar uma mensagem qualquer. Ex:
{
    "candidato": "Olá!"
}
</pre>
