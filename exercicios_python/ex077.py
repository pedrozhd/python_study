
listagem = ('aprender', 'brincar', 'cozinhar', 'desenhar', 'estudar', 'falar', 'ganhar')

for elemento in range(0, len(listagem)):
        print(f'\nNa palavra {listagem[elemento]}, temos ', end='')
        for letra in listagem[elemento]:
            if letra.lower() in 'aeiou':
                print(letra, end=' ')