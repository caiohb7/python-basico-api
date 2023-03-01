import requests
import json
import time
import datetime


def cotacao_dolar():
    req = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL')
    dicionario = json.loads(req.text)
    return dicionario


def cotacao_euro():
    req = requests.get('https://economia.awesomeapi.com.br/last/EUR-BRL')
    dicionario = json.loads(req.text)
    return dicionario


def cotacao_bitcoin():
    req = requests.get('https://economia.awesomeapi.com.br/last/BTC-BRL')
    dicionario = json.loads(req.text)
    return dicionario


while True:
    print(datetime.datetime.now(), '\n')
    # print('USD:', cotacao_dolar()['USDBRL']['bid'], 'BRL')
    # print('EUR:', cotacao_euro()['EURBRL']['bid'], 'BRL')
    print('BTC:', cotacao_bitcoin()['BTCBRL']['bid'], 'BRL\n\n')
    time.sleep(2)
