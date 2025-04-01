import random
import time

# usei a função randint para o computador sortear um número de 0 a 5.
num = random.randint(0, 5)

usu = int(input('Digite um número de 0 a 5: '))

print('Processando...'), time.sleep(0.5)

# se o número que o usuário colocou for igual ao da máquina, usuário vence.
if usu == num:
    print('Parabéns, você venceu a máquina!')
else:
    print(f'Eu pensei no {num}. Tente novamente. Você perdeu!')