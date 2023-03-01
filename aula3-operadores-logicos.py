idade = int(input('Digite a sua idade: '))
peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))

if idade >= 18 and peso >= 60.0 and altura >= 1.70:
    print('Você está apto a servir ao Exército.')
else:
    print('Você não está apto a servir ao Exército.')