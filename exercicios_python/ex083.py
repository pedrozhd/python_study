

lista = list()
exp = input('Expressão: ')

for i in exp:
    if i == '(' or i == ')':
        lista.append(i)

check = 0
for v in lista:
    if v == '(':
        check += 1

    if v == ')':
        check -= 1

if check > 0:
    print('Expressão inválida.')

else:
    print('Expressão válida.')