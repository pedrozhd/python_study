p = int(input('Digite o seu primeiro número: '))
s = int(input('Digite o seu segundo número: '))
t = int(input('Digite o seu terceiro número: '))

if p > s and s > t:
    print(f'Esse {p} é o maior e esse {t} é o menor')

elif p > t and s < t:
    print(f'Esse {p} é o maior e esse {s} é o menor')

elif s > p and p > t:
    print(f'Esse {s} é o maior e esse {t} é o menor')

elif s > t and p < t:
    print(f'Esse {s} é o maior e esse {p} é o menor')

elif t > p and s < p:
    print(f'Esse {t} é o maior e esse {s} é o menor')

elif t > s and p < s:
    print(f'Esse {t} é o maior e esse {p} é o menor')

print('============ Fim =============')