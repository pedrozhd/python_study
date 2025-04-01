# aproveitamento

jog = dict()
soma = 0
gols = list()

while True:
    try:
        jog['nome'] = input('Nome: ')
        jog['partidas'] = int(input(f'Total de partidas de {jog['nome']}: '))

        for n in range(jog['partidas']):
            gols.append(int(input(f'Total de gols na {n + 1}° partida: ')))

        for g in gols:
            soma += g

        jog['gols'] = gols    
        jog['total'] = soma

        print('\nEstatísticas.')
        for k, v in jog.items():
            print(f'{k} = {v}')

        print('\n')
        print('=' *20)
        print(f'O jogador {jog['nome']} jogou ao todo {jog['partidas']} partidas.')

        for c in range(jog['partidas']):
                print(f'Na partida {c + 1}, fez {gols[c]} gols!')

        print(f'Foi um total de {jog['total']} gols.')
        break

    except ValueError:
        print('Comando inválido')
       


