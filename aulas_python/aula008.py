# trabalhando com módulos

import math # importa toda a biblioteca
from math import sqrt, ceil, floor # importa apenas o item desejado após o import
# ceil arredonda para cima
# floor arredonda para baixo

num = int(input('Digite um número: '))
raiz1 = math.sqrt(num)
raiz = math.ceil(sqrt(num)) # sem o math. pois foi o único item importado 

print(ceil(raiz))
print(math.ceil(raiz))

# ------------------------------------------------------------------------------------------

import random

num2 = random.random() # gera número aleatório
num3 = random.randint(1, 10) # gera 1 número entre 1 e 10

print(num2)
print(num3)

print(random.randint(20, 50)) # pode ser feito dessa forma tb

# ------------------------------------------------------------------------------------------

import emoji

print(emoji.emojize('Olá, Mundo! :earth_americas:', use_aliases=True))
print('Olá, Mundo! 🌎')