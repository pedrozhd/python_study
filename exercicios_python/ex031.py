dis = float(input('Qual a distância da sua viagem? '))

if dis <= 200:
    print(f'Aqui está o preço da sua passagem: R${dis * 0.50:.2f}')
else:
    print(f'Aqui está o preço da sua passagem: R${dis * 0.45:.2f}')