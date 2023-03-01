import re  # regular expression
import requests

req = requests.get('http://www.mcce.org.br/newsletter')

padrao = re.findall(r'[\w\._-]+@[\w-]+\.[\w\._-]+', req.text)

if padrao:
    for i in padrao:
        print(i)
else:
    print('Padrão não encontrado')
