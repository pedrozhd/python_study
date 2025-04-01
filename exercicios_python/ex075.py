# estatística

while True:
    try:
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite mais um número: '))
        n3 = int(input('Digite outro número: '))
        n4 = int(input('Digite o último número: '))
        break
    except ValueError:
        print('Comando Inválido.')

lista = (n1, n2, n3, n4)
pares = []

print(f'O número 9 apareceu {lista.count(9)} vez(es).')

if 3 not in lista:
    print('O número 3 não corresponde a nenhuma posição.')
else:
    print(f'O número 3 aparece na {lista.index(3) + 1}º posição.')

for c in lista:
    if c % 2 == 0:
        pares.append(c)

if pares:
    print(f'Os números pares digitados foi/foram:', *pares, sep=' ')

else:
    print('Não há números pares.')

