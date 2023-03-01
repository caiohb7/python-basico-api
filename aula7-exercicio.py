def maior(colecao):
    maior_item = colecao[0]
    for i in colecao:
        if i > maior_item:
            maior_item = i
    return maior_item


print(maior([2, 5, 7.89, 8, 325, -254, 798]))


def menor(colecao):
    menor_item = colecao[0]
    for i in colecao:
        if i < menor_item:
            menor_item = i
    return menor_item


print(menor([2, 5, 7.89, 8, 325, -254, 798]))
