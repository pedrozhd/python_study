def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))

        except (ValueError, TypeError):
            print('Erro. Número inválido.')
            continue
        
        except KeyboardInterrupt:
            print('\nEntrada de dados interrompida pelo usuário.')
            return 0
        
        else:
            return n
        
def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))

        except (ValueError, TypeError):
            print('Erro. Número inválido.')
            continue
        
        except KeyboardInterrupt:
            print('\nEntrada de dados interrompida pelo usuário.')
            return 0
        
        else:
            return n


n = leiaInt('Digite um número: ')
n1 = leiaFloat('Digite um número quebrado: ')
print(f'O valor inteiro e o quebrado digitado foram: {n} e {n1}')