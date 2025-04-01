# leitor de número e soma de pares

s = 0
numeros_pares = []

for c in range(1, 7):
    numero_qualquer = int(input( # faço a leitura dos números
        f'Digite o {c}° número: '
    ))
    if numero_qualquer % 2 == 0: # verifico se é um número par
        s += numero_qualquer # faço a soma apenas dos números pares
        numeros_pares.append(numero_qualquer) # após verificação, armazena os pares na variável numeros_pares

print('=' * 45)
print('Números pares digitados:', numeros_pares)
print(f'O valor da soma dos números pares é de: {s}')