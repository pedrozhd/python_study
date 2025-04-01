sal = float(input('Escreva o seu salário: '))

if sal > 1250:
    au1 = sal * (110/100)
    print(f'Com o aumento de 10% o seu salário saiu de R${sal} para R${au1:.2f}')
else: 
    au2 = sal * (115/100)
    print(f'Com o aumento de 15% o seu salário saiu de R${sal} para R${au2:.2f}')

print('============ Fim ============')