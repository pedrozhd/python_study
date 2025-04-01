
valores = list()

maior = menor = 0

for p in range(0, 5):
    valores.append(int(input(f'Digite um valor para a {p + 1}° posição: ')))

    '''if p == 0:
        maior = menor = valores[p]
    else:
        if valores[p] > maior:
            maior = valores[p]
        if valores[p] < menor:
            menor = valores[p]'''
 
  
print(f'Aqui está a sua lista: {valores}.')
print(f'O maior número da lista é o {max(valores)} e está na posição: ', end='')

for indice, valor in enumerate(valores):
    if valor == max(valores):
        print(f'{indice + 1}... ', end='')

print()
print(f'O menor número da lista é o {min(valores)} e está na posição: ', end='')

for indice, valor in enumerate(valores):
    if valor == min(valores):
        print(f'{indice + 1}... ', end='')