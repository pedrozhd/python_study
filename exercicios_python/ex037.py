# entrada para número
numero_inteiro = int(input('Digite um número inteiro: '))

# escolha de opções
sua_opcao = int(input(
    'Escolha uma das opções abaixo:\n'
    '[ 1 ] Converter para BINÁRIO\n'
    '[ 2 ] Converter para OCTAL\n'
    '[ 3 ] Converter para HEXADECIMAL\n'
    'Sua opção: '
))

# verico se o comando é inválido
if sua_opcao not in [1, 2, 3]:
    print('Comando inválido. Tente novamente.')

else:
    # verifico a qual opção o número se refere
    if sua_opcao == 1:
        print(f'O número {numero_inteiro} em BINÁRIO é {bin(numero_inteiro)[2:]}')

    elif sua_opcao == 2:
        print(f'O número {numero_inteiro} em OCTAL é {oct(numero_inteiro)[2:]}')

    else:
        print(f'O número {numero_inteiro} em HEXADECIMAL é {hex(numero_inteiro)[2:]}')