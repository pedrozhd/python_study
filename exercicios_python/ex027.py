nom = str(input('Escreva seu nome completo: '))

# usei a função SPLIT para dividir e eu pegar o objeto na primeira posição [0]
print(f'Aqui está o seu primeiro nome: {nom.split()[0]}')

# da mesma forma eu usei split, mas para pegar o último objeto eu usei a psoição [-1]
print(f'Aqui está o seu último nome: {nom.split()[-1]}')