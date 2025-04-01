nom = str(input('Digite seu nome compelto: '))

print(f'Aqui está seu nome completo em letras maiúsculas: {nom.upper()}')
print(f'Aqui está seu nome completo em letras minúsculas: {nom.lower()}')

# contei o número usando a função LEN e a função REPLACE para substituir os espaços para sem espaços
print(f'Aqui está quantas letras tem em seu nome: {len(nom.replace(' ', ''))}')

# usei a função LEN de leitura de caractere com a função SPLIT de separar uma string, li somente a string
# separada na primeira posição [0]
print(f'Seu primeiro nome tem {len(nom.split()[0])} letras!')