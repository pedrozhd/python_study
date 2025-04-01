# aprimoramento da matriz

matriz = [[0, 0, 0], [0, 0 ,0], [0, 0, 0]]

for linha in range(0, 3):
    for coluna in range(0, 3):
        while True:
            try:
                matriz[linha][coluna] = int(input(f'Digite um valor para a posição [{linha}, {coluna}]: '))
                break
            except ValueError:
                print('Entrada Inválida.')

print('\nMatriz 3x3: ')
for linha in matriz:
    print(linha)

p = 0
for v in matriz[0]:
    if v % 2 == 0:
        p += v

for v in matriz[1]:
    if v % 2 == 0:
        p += v

for v in matriz[2]:
    if v % 2 == 0:
        p += v

print('\nEstatísticas: ')
print(f'A soma dos valores pares é: {p}')
print(f'O maior valor da segunda linha é o: {max(matriz[1])}')
print(f'A soma dos valores da terceira coluna é: {matriz[0][2] + matriz[1][2] + matriz[2][2]}')
