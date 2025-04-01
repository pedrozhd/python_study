
n = list()


while True:
    try:
        n.append(int(input('Digite um número: ')))

    except ValueError:
        print('Comando Inválido.')

    while True:
        perg = input('Quer continuar [S/N]? ').upper().strip()
        if perg in ('S', 'N'):
            break
        else:
            print('Letra Inválida.')
        
    if perg == 'N':
        break

print(f'Foram digitados {len(n)} número(s).')
print(f'Lista ordenada de forma descrescente: {sorted(n, reverse=True)}')

if 5 in n:
    print(f'O 5 está na lista e foi digitado {n.count(5)} vez(es).')
else:
    print('O 5 não está na lista.')
