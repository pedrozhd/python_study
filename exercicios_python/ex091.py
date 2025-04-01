# maior valor sorteado
from random import randint
from time import sleep
from operator import itemgetter

jog = dict()

for j in range(0, 4):
        valor_sorteado = randint(1, 6)
        jog[f'Jogador{j + 1}'] = valor_sorteado

ranking = dict()       
print('=' * 25)
print('Ranking dos Jogadores!')
for k, v in jog.items():
    print(f'{k} = {v}')

print('-' * 25)

print('\n' + '=' * 25)

'''
O itemgetter é uma função do módulo operator que retorna um callable (algo que pode ser chamado como uma função).
Ele é usado para acessar elementos de uma sequência (como listas, tuplas ou dicionários) de forma eficiente.
Por exemplo, itemgetter(1) cria uma função que, quando chamada com uma tupla, retorna o segundo elemento da tupla.
'''

ranking = sorted(jog.items(), key = itemgetter(1), reverse = True)
for i, (jogador, valor) in enumerate(ranking):
      print(f'{i + 1}° lugar: {jogador} com {valor}.')
      sleep(1)

print('-' * 25)