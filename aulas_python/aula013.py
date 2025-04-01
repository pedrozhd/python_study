# estrutura de repetição for

for c in range(0, 6): # no último número o programa para, portanto sempre começar com 0
    print('O Pedro é maravilhoso!')
print('Fim.')

for c in range(1, 11): # contagem de 1 até o 10, por exemplo
    print(c)

for c in range(7, 0, -1): # informando a aliteração com -1, tirando 1 conforme roda o programa
    print(c)

for c in range(1, 11, 2): # pulando de 2 em 2
    print(c)

# entrada de um número
numero_qualquer = int(input(
    'Digite um número: '
))

for c in range(0, numero_qualquer + 1): # repetição até parar no número declarado
    print(c) # +1 para entrar na ordem correta

if numero_qualquer == 9:
    for c in range(0, numero_qualquer + 1):
        print(c)
else:
    print('Tente o número 9.')

s = 0
for c in range (0, 3): # esse comando executa 3 vezes o que está na indentação 
    numero_qualquer = int(input(
        'Digite um número:'
    ))
    s = s + numero_qualquer # ou s += numero_qualquer
print(f'Esse é o valor da soma dos números: {s}')
print('Fim.')