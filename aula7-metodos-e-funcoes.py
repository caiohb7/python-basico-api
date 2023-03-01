def soma(num1, num2):
    resp = num1 + num2
    return resp


retorno = soma(5.18, 6)

print(retorno)


def imprime_oi():
    print("oi")


imprime_oi()


def tem_sete_itens(item):
    if len(item) == 7:
        return True
    else:
        return False


print(tem_sete_itens("aaaaaaa"))
