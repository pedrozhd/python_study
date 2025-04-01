# números aleatórios
from random import randint

lista = (
    randint(1, 10), 
    randint(1, 10), 
    randint(1, 10),
    randint(1, 10),
    randint(1, 10)
)

lista = tuple(randint(1, 10) for _ in range(5))

print(f'Aqui está os número que foram listados: {lista}', sep=', ')
print(f'Aqui está o maior número {max(lista)} e aqui está o menor {min(lista)}')

