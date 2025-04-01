# tabuada utilizando for

numero_tabuada = int(input(
    'Escolha o número da sua tabuada: '
))

for c in range(1, 11):
    print(f'{numero_tabuada} * {c:2} = {numero_tabuada * c}')