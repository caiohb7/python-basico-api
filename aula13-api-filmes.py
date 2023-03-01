import requests
import json


def requisicao(titulo):
    requisicoes = requests.get(f'http://www.omdbapi.com/?t={titulo}&type=movie&apikey=d120712b')
    dicionario = json.loads(requisicoes.text)
    return dicionario


def printar_detalhes(filme):
    for i in filme:
        print(f'{i}: {filme[i]}')


sair = False

while not sair:
    digita_filme = input('Digite o nome do filme ou digite \'sair\': ')

    if digita_filme.casefold() == 'sair'.casefold():
        sair = True
    else:
        filme = requisicao(digita_filme)

        if filme['Response'] == 'False':
            print('Movie not found')
        else:
            printar_detalhes(filme)
