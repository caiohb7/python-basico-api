import sys

argumentos = sys.argv


def soma(num1, num2):
    return num1 + num2


def subtrai(num1, num2):
    return num1 - num2


if argumentos[1] == "soma":
    resp = soma(float(argumentos[2]), float(argumentos[3]))
elif argumentos[1] == "subtrai":
    resp = subtrai(float(argumentos[2]), float(argumentos[3]))

print(resp)
