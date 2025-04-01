from random import randint

numeros = list()

def sorteia():
    print('Sorteando 5 valores: ', end='')
    for _ in range(5):
        numeros.append(randint(1, 10))
    print(numeros)

def somaPar():
    print(f'Somando os valores pares de {numeros} - temos: ', end='')
    soma = 0
    for v in numeros:
        if v % 2 == 0:
            soma += v
    print(soma)

sorteia()
somaPar()
