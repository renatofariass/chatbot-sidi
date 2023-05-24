## Para rodar o projeto

1 - Instale o Python (> 3 version)

2 - Instale o PIP

3 - Instale a VirtualEnv
 - pip install virtualenv

4 - Crie uma virtual env chamada 'venv'
- python -m virtualenv venv 
- python3 -m virtualenv venv (linux)

5 - ative a virtual env


### Virtual ENV (Windows)


``` 
$ virtualenv venv
```
ATIVAR:
```
$ cd venv
$ cd Scripts
$ activate
```
DESATIVAR:
```
$ deactivate
```
Obs: Volte para a pasta principal após a ativação usando "cd .." até chegar no diretório 
principal para instalar as depêndencias do requirements.txt


### Virtual ENV (Linux)


``` 
$ virtualenv venv
```
ATIVAR:
```
$ source venv/bin/activate 
```
DESATIVAR:
```
$ deactivate
```

6 - Instale as dependências do projeto

``` 
pip install -r requirements.txt
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

## pergunta_controller

### criar perguntas (/perguntas/create/{id_da_vaga}) [POST]
<pre>
cria perguntas para uma determinada vaga. Ex. de como criar uma vaga via requisicão post:
{
    "eliminatoria": true,
    "pergunta": "pergunta?"
}
</pre>

#### obs¹: Você pode botar quais perguntas quiser e indicar como eliminatória ou não. Porém, as seguintes perguntas são obrigatórias (insira elas exatamente como estão abaixo (um por vez)) para que as informações do candidato sejam salvas no banco de dados corretamente:
<pre>
{
    "eliminatoria": false,
    "pergunta": "Qual seu nome?"
}
{
    "eliminatoria": false,
    "pergunta": "Qual é o seu email?"
}
{
    "eliminatoria": false,
    "pergunta": "Qual o seu linkedin?"
}
{
    "eliminatoria": false,
    "pergunta": "Qual o seu github?"
}
{
    "eliminatoria": false,
    "pergunta": "Qual sua formação?"
}
{
    "eliminatoria": false,
    "pergunta": "Fale sobre quais tecnologias você possui conhecimentos."
}
</pre>

#### obs²: Na última pergunta inserida nas vagas (não é obrigatório), mas eu recomendo que você use uma pergunta eliminatória no final para o candidato confirmar sua inscrição. Ex:
<pre>
{
    "eliminatoria": true,
    "pergunta": "Você quer confirmar a inscrição para essa vaga? Responda com '1' para Sim ou '0' para Não."
}
</pre>

#### obs³: Nas perguntas eliminatórias o chatbot só reconhece "sim" ou "não" como "1" ou "0", qualquer outra resposta a não ser essa o chatbot irá repetir a pergunta até o candidato digitar "0" ou "1".


### listar perguntas da vaga (/perguntas/vaga/{id_da_vaga}) [GET]
<pre>
Lista todas as perguntas de uma determinada vaga. Ex. de retorno:
[
    {
        "eliminatoria": true,
        "pergunta": "pergunta?"
    },
    {
        "eliminatoria": true,
        "pergunta": "pergunta2?"
    }
]
</pre>



## bot_controller

### chatbot (/chatbot) [POST]
<pre>
Para iniciar a conversa com o chtatbot você precisa mandar uma mensagem qualquer. Ex:
{
    "resposta": "Olá!"
}
</pre>
