c1 = float(input('Primeira reta: '))
c2 = float(input('Segunda reta: '))
c3 = float(input('Terceira reta: '))

if (c1 + c2) <= c3:
    print('Não pode formar um triângulo.')
elif (c1 + c2) > c3:
    print('Pode formar um triângulo.')
elif (c2 + c3) <= c1:
    print('Não pode formar um triângulo.')
elif (c2 + c3) > c1:
    print('Pode formar um triângulo.')
elif (c1 + c3) <= c2:
    print('Não pode formar um triângulo.')
elif (c1 + c3) > c2:
    print('Pode formar um triângulo.')

print('========== Fim ==========')