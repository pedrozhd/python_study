
normal_list = list()
par_list = list()
impar_list = list()


while True:
    try:
        num = int(input('Digite um número: '))
        normal_list.append(num)
    except ValueError:
        print('Comando Inválido.')

    while True:
        pergunta = input('Quer continuar [S/N]? ').upper().strip()

        if pergunta in ('S', 'N'):
            break
        else:
            print('Letra inválida.')

    if pergunta == 'N':
        break

print(f'Aqui está a sua lista: {normal_list}')

for v in normal_list:
    if v % 2 == 0:
        par_list.append(v)

    else:
        impar_list.append(v)

print(f'Sua lista de números pares: {par_list}')
print(f'Sua lista de números ímpares: {impar_list}')