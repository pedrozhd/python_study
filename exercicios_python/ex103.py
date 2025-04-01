

def ficha(n, g):
    if n.strip() == '':
        n = '<desconhecido>'

    if g.isnumeric():
        g = int(g)

    else:
        g = 0

    print(f'O jogador {n} fez {g} gol(s) no campeonato. ')

ficha(input('Nome: '), input('Número de gols: '))
