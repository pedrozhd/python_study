# variáveis compostas (tuplas)

# as tuplas são imutáveis

# tuplas podem ser sem parentêses
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')

print(lanche[1:3]) # descarta o terceiro índice

print(lanche[-1]) # mostra o último

print(lanche[1:]) # índice 1 até o final

print(lanche[:2]) # zero até o índice 2, mas descarta o elemento 2

print(len(lanche)) # conta o número de elementos

print(*sorted(lanche)) # organiza em ordem alfabética

print('-=' * 30) 

# remove os parentêses
# método simples sme definir posição
for c in lanche:
    print(f'Eu vou comer {c}!')

print('-=' * 30) 

# ou

print(*lanche)

# ou

print(*lanche, sep=', ', end='.\n')
# sep = define o separador das palavras
# end = define o fim

print('-=' * 30) 

# utilização do len + for
for contador in range(0, len(lanche)):
    # print(contador) # conta os elementos de 0 até  a leitura de elementos de lance
    print(f'Vou comer {lanche[contador]}, na posição {contador}!') # printa o nome dos elementos em cada posição 

print('-=' * 30)

# enumerate define a numeração e o nome para cada posição
for posicao, comida in enumerate(lanche):
    print(f'Vou comer {comida}, na posição {posicao}!')

print('-=' * 30) 

a = (2, 5, 4)
b = (5, 8 , 1, 2)
c = a + b # junção de tuplas
print(c)
print(len(c)) # lê a quantidade de elementos da tupla
print(c.count(5)) # número de vezes em que o número 5 aparece
print(c.index(8)) # em que posição está

pessoa = ('pedro', 18, 'm', 80.5)
del(pessoa) # deleta a tupla
