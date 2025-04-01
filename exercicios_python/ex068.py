import random

contador = 0

while True:
    escolha_maquina = random.randint(1, 10) 
    sua_escolha = str(input('Você quer Par ou Ímpar [P/I]? ')).title().strip()
    seu_numero  = int(input('Digite o seu número: '))
    resultado = seu_numero + escolha_maquina
    print(f'Você jogou {seu_numero} e o computador jogou {escolha_maquina}. O total deu {resultado}.')
    print('-=' * 30)

    if sua_escolha not in 'Ii':
        if resultado % 2 == 0:
            print('Deu par. Você ganhou!')
            print('Vamos novamente...')
            print('-=' * 30)
            contador += 1
        else:
            print('Deu ímpar. Você perdeu!')
            break

    elif sua_escolha not in 'Pp':
        if resultado % 2 != 0:
            print('Deu ímpar. Você ganhou!')
            print('Vamos novamente...')
            print('-=' * 30)
            contador += 1
        else:
            print('Deu par. Você perdeu!')
            break

print(f'Game Over. Você venceu {contador} veze(s) seguida(s)!')