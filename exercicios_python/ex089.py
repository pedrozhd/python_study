# boletim

new_bol = []

while True:
    try:
        # validção do nome
        nome = input('Nome: ').strip()
        if not nome:
            print('O nome não pode estar vazio. Tente novamente.')
            continue

        nota1 = float(input('Nota 1: '))
        nota2 = float(input('Nota 2: '))

        # validação das notas
        if not (0 <= nota1 <= 10) or not (0 <= nota2 <= 10):
            print('As notas devem estar entre 0 e 10. Tente novamente.')
            continue

        media = (nota1 + nota2) / 2
        new_bol.append([nome, [nota1, nota2], media])

        # validação de entrada
        pergunta = input('Quer continuar [S/N]? ').upper().strip()
        while pergunta not in ['S', 'N']:
            print("Digite 'S' para continuar ou 'N' para sair.")
            pergunta = input('Quer continuar [S/N]? ').upper().strip()

        if pergunta == 'N':
            break

    except ValueError:
        print('Erro: Digite um valor numérico válido para as notas.')

print('\n' + '=' * 30)
print(f'{"No.":<4} {"Nome":<8} {"Média":>10}')
print('-' * 30)


for pos, v in enumerate(new_bol):
    print(f'{pos:<4} {v[0]:<8} {v[2]:>10.1f}')

print('=' * 30 + '\n')

# consulta de notas
while True:
    try:
        indice_aluno = int(input('Deseja mostrar a nota de algum aluno (999 interrompe)? '))
        
        if indice_aluno == 999:
            break

        if 0 <= indice_aluno < len(new_bol):
            print(f'As notas de {new_bol[indice_aluno][0].capitalize()} são: {new_bol[indice_aluno][1]}')
        else:
            print(f'Erro: Índice inválido. Digite um número entre 0 e {len(new_bol) - 1}.')

    except ValueError:
        print('Erro: Digite um número válido.')