# mega-sena
from random import randint
from time import sleep

# perguntas a quantidade de palpites
pp = int(input('Deseja gerar quantos palpites? '))
print('\n')

print(5 * '-=', f'Gerando {pp} palpites', '-=' * 5)
print('\n')

# looping para gerar cada palpite
for _ in range(pp):
    palpites = [] # cria uma nova lista para o palpite atual

    while len(palpites) < 6: # garante que o palpite terá 6 números
        numero = randint(1, 60) # gera um número aleatório entre 1 e 60
        if numero not in palpites: # verifica se o número já está no palpite
            palpites.append(numero) # adiciona o número ao palpite

    sleep(0.5)
    print(palpites)
print('\n')