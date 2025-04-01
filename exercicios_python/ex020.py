import random

nome1 = str(input('Insira o nome do seu primeiro aluno: '))
nome2 = str(input('Insira o nome do seu segundo aluno: '))
nome3 = str(input('Insira o nome do seu terceiro aluno: '))
nome4 = str(input('Insira o nome do seu quarto aluno: '))

# lista com os nomes lidos
nomes = [nome1, nome2, nome3, nome4]

# embaralha a lista
random.shuffle(nomes)

print('-' * 20)

# com a lista nova, escolhe os termos
print(f'A ordem de aprensetação é:')
print(f'1° --> {nomes[0]}')
print(f'2° --> {nomes[1]}')
print(f'3° --> {nomes[2]}')
print(f'4° --> {nomes[3]} ')