from time import sleep

vel = int(input('Qual a velocidade que o vacilão passou no radar? '))

print('Processando...')
sleep(2)

# se a valocidade for menor ou igual a 80 ele toma multa.
if vel >= 80: 
    print('Parabéns, sua Anta. Você acaba de ser multado!')
    print(f'O valor da sua querida multa é de: R${(vel - 80) * 7}.')
else:
    print('Você se safou dessa vez, seu pilantra.')
print(f'Você passou a {vel}KM/h, em um radar de 80KM/h.')