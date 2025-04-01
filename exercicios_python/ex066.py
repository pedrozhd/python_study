# soma e contador desconsiderando o flag 

s = c = 0
while True: # executa sempre
    num = int(input('Digite um número: '))

    if num == 999: # se o flag for 999 o programa é interrompido
        break
    else:
        s += num
        c += 1
print(f'Foram digitados {c} número(s), e a soma entre eles deu {s}!')