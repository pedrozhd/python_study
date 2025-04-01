def leiaInt():
    while True:
        try:
            n = int(input('Digite um número: '))
            print(f'Você acabou de digitar o número {n}')
            break
        
        except ValueError:
            print('Erro. Apenas números são aceitos.')

leiaInt()