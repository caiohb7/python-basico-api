import requests

cabecalho = {'user-agent': 'Caio',
             'referer': 'https://www.google.com.br'}
dados = {'username': 'caio',
         'password': '12345678'}
try:
    requisicao = requests.post('https://putsreq.com/LCPDjVgaSEDCM8AEappi',
                               headers=cabecalho,
                               data=dados)
    print(requisicao.text)
except Exception as e:
    print(f'Error: {e}')


