# matriz 3 x 3

vertical1 = [[], [], []]
vertical2 = [[], [], []]
vertical3 = [[], [], []]

for c in range(0, 3):
    vertical1[c].append(int(input(f'Digite um valor na [0, {c}]: ')))

for c in range(0, 3):
    vertical2[c].append(int(input(f'Digite um valor na [1, {c}]: ')))

for c in range(0, 3):
    vertical3[c].append(int(input(f'Digite um valor na [2, {c}]: ')))

print('\n')
print(vertical1[0], vertical1[1], vertical1[2])
print(vertical2[0], vertical2[1], vertical2[2])
print(vertical3[0], vertical3[1], vertical3[2])

# versão otimizada

matriz = [[0, 0, 0], [0, 0 ,0], [0, 0, 0]]

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para a posição [{linha}, {coluna}]: '))

print('\nMatriz 3x3: ')
for linha in matriz:
    print(linha)