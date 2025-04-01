num1 = float(input('Digite um número: '))
num2 = float(input('Digite outro número: '))

if num1 > num2:
    print(f'O {num1:.1f} é maior que o {num2:.1f}.')

elif num1 < num2:
    print(f'O {num2:.1f} é maior que o {num1:.1f}.')

else:
    print('Os dois são iguais.')