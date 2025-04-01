cas = float(input('Qual o valor da casa? '))
sal = float(input('Qual é o seu salário? '))
ano = float(input('Em quantos anos você pretende pagar? '))

tempo = ano * 12
prestação = cas / tempo
negado = sal * (30/100)

if prestação > negado:
    print('O seu empréstimo foi recusado.')
    print(f'Em razão da prestação (R${prestação:.2f}) exceder o valor de 30% do seu salário (R${negado:.2f}).')

else:
    print(f'O seu empréstimo foi aceito, o valor da prestação é de R${prestação:.2f}.')
