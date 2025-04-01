# variáveis compostas (listas)
# as listas são mutáveis

from random import randint

# lista = list(randint(1, 10) for _ in range(10)) # isso é uma lista - mutável
# tupla = tuple(randint(1, 10) for _ in range(10)) # isso é uma tupla - imutável
 
# print(lista)
# print(tupla)

lista1 = list(range(1, 6))
 
lista1.append(6) # adicionando o 6 dentro da lista, no final

# isso retorna novos índices
lista1.insert(0, 10) # adicionando o 10 no índice anterior ao 0

# isso retorna novos índices
lista1.insert(1, 9) # adicionando o 9 no índice 2, entre o 1 e o 3

lista1[0] = 2 # altera o valor de índice 0 para o valor 2

lista1.sort() # coloca os valores em ordem
lista1.sort(reverse=True) # coloca em ordem contrária

lista1.pop() # remove o último elemento, quando não há parâmetros
lista1.remove(2) # remove a primeira ocorrência do número 2

print(lista1)
print(f'Essa lista tem {len(lista1)} elementos.')

valores = list()
valores.append(5)
valores.append(9)
valores.append(4)

print(valores)
for v in range(0, 5):
    valores.append(int(input('Digite um valor: '))) # chamo o comando colocando na lista de forma automática

for e, v in enumerate(valores):
    print(f'Na posição {e} eu encontrei o valor {v}.')
print('Final da lista')

a = [2, 3, 4, 7]
b = a[:] # gera uma cópia, invés de criar uma ligação
b[2] = 8 

print(f'Lista A: {a}')
print(f'Lista B: {b}')