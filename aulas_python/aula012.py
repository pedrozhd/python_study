# condições aninhadas

nome = str(input('Digite seu nome: ')).title()

if nome == 'Pedro':
    print('Seu nome é maravilhoso.')
    print(f'Tenha um ótimo dia, {nome}!')

elif nome == 'Luiza' or nome == 'Michele' or nome == 'Douglas':
    print(f'Seu nome é legal.')
    print(f'Tenha um bom dia, {nome}!')

elif 'Júlia' or 'Ana' or 'Claúdia' in nome:
    print('Um dos nomes femininos mais usados.')
    print(f'Tenha um bom dia, {nome}!') 

else:
    print(f'Tenha um mal dia, {nome}. Seu(a) merda!')
