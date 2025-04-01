# manipulção de pares e ímpares

numeros = [[], []]

for c in range(0, 7):
    while True:
        try:
            n = int(input(f'Digite o {c + 1}° número: '))
            if n % 2 == 0:
                numeros[0].append(n)
            else:
                numeros[1].append(n)
            break
        
        except ValueError:
            print('Digite apenas números.')

print(f'Pares: {sorted(numeros[0])}')
print(f'Ímpares: {sorted(numeros[1])}')