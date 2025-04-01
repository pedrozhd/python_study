from random import choice

# resolução chatgpt

# entrada da minha opção
minha_opcao = str(input('Pedra, Papel ou Tesoura: ')).title().strip()

# opções em uma lista, para usar a função choice
opcoes = ['Pedra', 'Papel', 'Tesoura']

if minha_opcao not in opcoes: # não é o inverso, porque iria verificar se a lista inteira estava dentro de minha_opcao
    print('Comando inválido. Escolha entre: Pedra, Papel ou Tesoura')

else: 
    # opção da máquina
    opcao_maquina = (choice(opcoes))
    
    # exibe as escolhas 
    print(f'Essa é a minha opção: {minha_opcao}')
    print(f'Essa é a sua opção: {opcao_maquina}')

    # lógica do game
    if minha_opcao == opcao_maquina:
        print('Empatamos. Vamos tentar novamente.')

    elif (minha_opcao == 'Pedra' and opcao_maquina == 'Tesoura') or \
         (minha_opcao == 'Papel' and opcao_maquina == 'Pedra') or \
         (minha_opcao == 'Tesoura' and opcao_maquina == 'Papel'):
        print('Ganhei de você! 😁')

    else:
        print('Você ganhou de mim! 🥲')

# minha resolução

# entrada da minha opção
minha_opcao = str(input('Pedra, Papel ou Tesoura: ')).title()

# opções em uma lista, para usar a função choice
opcao = ['Pedra', 'Papel', 'Tesoura']

# entra da opção da máquina
opcao_maquina = (choice(opcao))

if minha_opcao == 'Pedra' and opcao_maquina == 'Tesoura':
    print('Ganhei :)')
    print(f'Minha opção: {minha_opcao}')
    print(f'Sua opção: {opcao_maquina}')

elif minha_opcao == 'Papel' and opcao_maquina == 'Pedra':
    print('Ganhei :)')
    print(f'Minha opção: {minha_opcao}')
    print(f'Sua opção: {opcao_maquina}')

elif minha_opcao == 'Tesoura' and opcao_maquina == 'Papel':
    print('Ganhei :)')
    print(f'Minha opção: {minha_opcao}')
    print(f'Sua opção: {opcao_maquina}')

elif minha_opcao == 'Pedra' and opcao_maquina == 'Papel':
    print('Perdi :(')
    print(f'Minha opção: {minha_opcao}')
    print(f'Sua opção: {opcao_maquina}')

elif minha_opcao == 'Papel' and opcao_maquina == 'Tesoura':
    print('Perdi :(')
    print(f'Minha opção: {minha_opcao}')
    print(f'Sua opção: {opcao_maquina}')

elif minha_opcao == 'Tesoura' and opcao_maquina == 'Pedra':
    print('Perdi :(')
    print(f'Minha opção: {minha_opcao}')
    print(f'Sua opção: {opcao_maquina}')

elif minha_opcao == opcao_maquina:
    print('Empatamos. Vamos novamente!')
    print(f'Minha opção: {minha_opcao}')
    print(f'Sua opção: {opcao_maquina}')

else:
    print('Comando inválido. Escolha entre: Papel, Pedra ou Tesoura')