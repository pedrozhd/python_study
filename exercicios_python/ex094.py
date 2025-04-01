# cadastro

lista_cadastro = list()
nome_mulheres = list()
acima_da_media = list()
soma_idades = 0

while True:
    try:
        cadastro = dict()
        cadastro['nome'] = input('Digite seu nome: ').capitalize()
        sexo = input('Digite seu sexo [M/F]: ').upper()
        if sexo in ['M', 'F']:
            cadastro['sexo'] = sexo
            break
        else:
            print('Entrada inválida. Digite apenas "M" ou "F".')

        idade = int(input('Digite a sua idade: '))
        if idade >= 0:
            cadastro['idade'] = idade
            break
        else:
            print('Digite números válidos.')
        

        soma_idades += cadastro['idade']

        if cadastro['sexo'] == 'F':
            nome_mulheres.append(cadastro['nome'])

        lista_cadastro.append(cadastro)

        pergunta = input('Quer continuar [S/N]? ').upper()
        if pergunta in ['S', 'N']:
            break
        
        else:
            print('Entrada inválida. Digite apenas "S" ou "N"')

    except ValueError:
        print('Apenas números são válidos.')

media = soma_idades / len(lista_cadastro)

for pessoa in lista_cadastro:
    if pessoa['idade'] > media:
        acima_da_media.append(pessoa)

print(f'\nNúmero total de pessoas cadastradas: {len(lista_cadastro)}')
print(f'A média de idade das pessoas cadastradas é: {media:.2f}')
print(f'As mulheres registradas foram: {nome_mulheres}')
print(f'As pessoas com idade acima da média são: ')
for p in acima_da_media:
    print(f'Nome: {pessoa['nome']} \nIdade: {pessoa['idade']}')