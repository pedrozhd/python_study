# adivinhação

from random import randint

# primeira interação do usuário
numero_da_maquina = randint(0, 10) # máquina pensa em um número de 0 a 10
numero_do_usuario = int(input('Tente adivinhar o número em que a máquina está pensando: '))
contador_de_palpites = 1 # vai contar o primeiro palpite aqui

if numero_do_usuario == numero_da_maquina:
    print(f'Você adivinhou de primeira. Eu pensei no número {numero_da_maquina}!')
    
else:
    
    # caso erre continua aqui
    while numero_do_usuario != numero_da_maquina: # enquanto forem diferentes o usuário tenta novamente
        numero_do_usuario = int(input('Errou. Tente adivinhar novamente: ')) # ocorre enquanto for diferente, False
        contador_de_palpites += 1

    # ocorre fora do looping, quando for True
    print(f'Você adivinhou em {contador_de_palpites} palpite(s). Eu pensei no número {numero_da_maquina}!')
