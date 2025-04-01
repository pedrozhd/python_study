# operadores aritméticos

# + -> adição
# - -> subtração
# * -> multiplicação
# / -> divisão
# ** -> potência
# // -> divisão inteira
# % -> resto da divisão


# ordem de precedência

# 1 - ()
# 2 - **
# 3 - * -- // -- % -- /
# 4 - + -- -

print('=' * 20)
print('hey' * 5)

n = input('Qual o seu nome: ')
print(f'Prazer, {n:20}!') # variável em 20 espaços
print(f'Prazer, {n:>20}!') # variável à direita
print(f'Prazer, {n:<20}!') # variável à esquerda
print(f'Prazer, {n:^20}!') # variável no centro
print(f'Prazer, {n:=^20}!') # variável no centro com = em volta

n1 = int(input('Digite um número: '))
n2 = int(input('Outro número: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

# \n -- quebra de linha
# end = ' ' -- junta linhas quebradas
print(f'A soma é {s}, \no produto é {m},\na divisão é {d:.3f}', end = '\n') # 3 casas decimais em caso de dízima
print(f'A divisão inteira é {di}, \na potência é {e}')
