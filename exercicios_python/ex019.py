import random

nome1 = str(input('Insira o nome do seu primeiro aluno: '))
nome2 = str(input('Insira o nome do seu segundo aluno: '))
nome3 = str(input('Insira o nome do seu terceiro aluno: '))
nome4 = str(input('Insira o nome do seu quarto aluno: '))
nomes = [nome1, nome2, nome3, nome4]


# choice escolhe apenas 1 da lista
print(f'O aluno sorteado foi: {random.choice(nomes)}')