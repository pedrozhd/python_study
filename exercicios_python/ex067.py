# tabuada descosiderando números negativos

while True:
    num = int(input('Deseja ver a tabuada de qual número? '))

    if num < 0:
        print('Comando Inválido!')
        break

    else:
        for c in range(1, 11):
            print(f'{num} x {c:2} = {num * c}' )
        print('-=' * 12)