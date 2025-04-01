# menus
from time import sleep

print('-' * 10, 'MENU', '-' * 10)
valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))

menu = 0
while menu != 5:

    sleep(1)
    print('-' * 26)
    menu = int(input(
    'O que você deseja fazer?\n'
    '[ 1 ] Somar\n'
    '[ 2 ] Multiplicar\n'
    '[ 3 ] Dividir\n'
    '[ 4 ] Digitar novos números\n'
    '[ 5 ] Fechar o programa\n'
    'Escolha a opção: '
    ))
    print('-' * 26)
    if menu > 5:
        print('Erro. Digite apenas: 1, 2, 3 ou 4.')
    
    else:
        if menu == 1:
            print(f'{valor1} + {valor2} = {valor1 + valor2}')
            
        elif menu == 2:
            print(f'{valor1} x {valor2} = {valor1 * valor2:.2f}')
            
        elif menu == 3:
            print(f'{valor1} / {valor2} = {valor1 / valor2:.2f}')

        elif menu == 4:
            valor1 = int(input('Digite o primeiro valor: '))
            valor2 = int(input('Digite o segundo valor: '))

print('Fim do Programa.')
