import requests
import json
import time


def sao_paulo():
    req = requests.get('https://api.hgbrasil.com/weather?format=json&key=181fe40f')
    dicionario = json.loads(req.text)
    return dicionario


def printa_clima():
    while True:
        print('Cidade:', sao_paulo()['results']['city'])
        print('Data:', sao_paulo()['results']['date'])
        print('Hora:', sao_paulo()['results']['time'])
        print('Clima:', sao_paulo()['results']['temp'], '°C')
        print('Umidade:', sao_paulo()['results']['humidity'], '%')
        print('Velocidade do vento:', sao_paulo()['results']['wind_speedy'], '\n')
        time.sleep(120)


printa_clima()
