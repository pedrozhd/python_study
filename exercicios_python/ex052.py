# minha resolução
# número primo
numero = int(input('Digite um número: '))

# verificando se é primo
for c in range(1, 10000):
    if numero % c == 0 and c != numero and c != 1:
        print('Não é primo!')

# resolução do chatgpt
divisores = 0 
for c in range(1, numero + 1):
    if numero % c == 0:
        print(c)
        divisores += 1 # conta quantos divisores tem o número

if divisores == 2:
    print(f'{numero} é um número primo.')
else:
    print(f'{numero} não é um número primo.')