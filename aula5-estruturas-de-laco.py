quantidade = int(input('Digite a quantidade de convidados: '))
lista_convidados = []

for i in range(quantidade):
    lista_convidados.append(input('Digite o nome do convidado: '))

print('\nLista de convidados: ')
for j in lista_convidados:
    print(j)
