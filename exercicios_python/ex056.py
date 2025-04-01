mulheres_20 = 0
maior_idade = []
media_idade = 0
nome_velho = []

for c in range(1, 5):
    nome = str(input(f'Nome da {c}ª pessoa: ')).strip()
    idade = int(input(f'Idade da {c}ª pessoa: '))
    sexo = str(input(f'Escolha F para Feminino e M para Masculino: ')).lower().strip()

    media_idade += idade

    
    if sexo  == 'f' and idade < 20:
        mulheres_20 += 1

    if sexo == 'm':
        maior_idade.append(idade)

    if idade == max(maior_idade):
        nome_velho = nome
media_idade = media_idade / 4


print(f'O nome do homem mais velho que possui {max(maior_idade)} anos é: {nome_velho.title()}!')
print(f'Essa é a idade média do grupo: {media_idade:.1f} anos') 
print(f'{mulheres_20} mulheres tem menos de 20 anos.')
