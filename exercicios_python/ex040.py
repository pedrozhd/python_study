n1 = float(input('Digite a sua nota: '))
n2 = float(input('Digite a sua outra nota: '))

m = (n1 + n2) / 2

if m < 5:
    print(f'Você foi reprovado. Sua média é de {m}.')

elif m == 5 or m < 6.9:
    print(f'Você está de recuperação. Sua média é de {m}.')

elif m >= 7:
    print(f'Parabéns, você foi aprovado. Sua média é de {m}.')