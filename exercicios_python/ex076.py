
listagem = (
    'Borracha', 2,
    'Lápis', 1.50,
    'Caneta', 2.75,
    'Estojo', 14,
    'Apontador', 5,
    'Caderno', 30,
)

# leitura do zero até o número total de elementos
for posicao in range(0, len(listagem)):

    if posicao % 2 == 0: # verifico se o índice do elemento é divisível por 2
        print(f'{listagem[posicao]:.<30}', end='') # pontos alinhados a esquerda

    else:
        print(f'R${listagem[posicao]:>6.2f}')