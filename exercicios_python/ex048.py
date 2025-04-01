# soma dos ímpares que são múltiplos de 3
contador = 0
soma_acumulativa = 0
for c in range(1, 501):
    if c % 3 == 0:
        if c % 2 != 0: # posso pular de 2 em 2, invés dessa condição
            contador += 1
            soma_acumulativa += c
print(f'A soma dos ímpares que são múltiplos de 3 ({contador}) é igual a: {soma_acumulativa}')