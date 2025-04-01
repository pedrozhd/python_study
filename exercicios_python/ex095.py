# aproveitamento

mais_jog = list()

while True:
    try: 
        # reinicializa a cada looping   
        jog = dict()
        gols = list()
        soma_gols = 0

        # cadastro do jogador
        jog['nome'] = input('Nome: ')
        partidas = int(input(f'Total de partidas de {jog['nome']}: '))

        # registro de gols por partida
        for n in range(partidas):
            gol = int(input(f'Total de gols na {n + 1}° partida: '))
            gols.append(gol)
            soma_gols += gol
            
        # adiciona os dados ao dicionário
        jog['gols'] = gols[:]    
        jog['total'] = soma_gols

        # adiciona o jogador a lista de jogadores
        mais_jog.append(jog.copy())


        while True:
            pergunta = input('Quer continuar [S/N]? ').upper()
            if pergunta in ['N', 'S']:
                break

            else:
                print('Entrada inválida. Digite apenas "S" ou "N".')

        if pergunta == 'N':
            break
        
    except ValueError:
        print('Comando inválido. Digite apenas números para partidas e gols.')
print('\n')


# exibição de dados
print('=' * 60)

# cabeçalho da tabela
print(f'{"Num.":<5}', end='')  # coluna do número
print(f'{"Nome":<15}', end='')  # coluna do nome
print(f'{"Partidas":<10}', end='')  # coluna de partidas
print(f'{"Gols":<20}', end='')  # coluna de gols
print(f'{"Total":<5}')  # coluna do total

print('=' * 60)

# corpo da tabela
for k, v in enumerate(mais_jog):
    print(f'{k:>3}  ', end='')  # número do jogador
    print(f'{v["nome"]:<15}', end='')  # nome do jogador
    print(f'{len(v["gols"]):<10}', end='')  # partidas do jogador
    print(f'{str(v["gols"]):<20}', end='')  # gols do jogador
    print(f'{v["total"]:<5}')  # total de gols

print('-' * 60)
print('\n')

# busca de um jogador específico
while True:
    try:
        busc = int(input('Deseja mostrar dados de qual jogador (999 interrompe)? '))
        if busc == 999:
            print('Finalizado.')
            break

        if busc >= len(mais_jog):
            print(f'Não existe jogador com o código: {busc}.')

        else:
            print('=' * 60)
            print(f'Levantamento do {mais_jog[busc]["nome"]}: ')
            print('=' * 60)

            for i, g in enumerate(mais_jog[busc]['gols']):
                print(f'No jogo {i + 1} fez {g} gols.')
            print('-' * 60)

    except ValueError:
        print('Comando inválido. Digite apenas números.')