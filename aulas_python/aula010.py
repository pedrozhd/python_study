# condições (parte 1)

# if --> se 
# else --> senão

# if carro.esquerda():
    # bloco True --> bloco verdadeiro
# else:
    # bloco False --> bloco falso

tempo = float(input('Quantos anos tem o seu carro? '))

if tempo <= 3:
    print('Seu carro está novo!')
else:
    print('Seu carro está velho!')
print('FIM.')

# -----------------------------------------------------------------

nome = str(input('Digite seu nome: ')).title().split()[0]

if nome == 'Pedro':
    print('Você é lindo!')
else:
    print('Que nome feio, igual você.')
print(f'Bom dia, {nome}!')

# ----------------------------------------------------------------

n1 = float(input('Digite a sua nota: '))
n2 = float(input('Digite a sua segunda nota: '))
r = (n1 + n2) / 2

if r >= 6:
    print('Que ótima nota, parabéns!')
else:
    print('Que péssimo nota, vai estudar.')