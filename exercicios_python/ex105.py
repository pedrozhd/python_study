

def notas(sit=True):
    ficha = list()
    ficha1 = dict()
    soma = 0

    for _ in range(4):
        ficha.append(float(input('Digite a sua nota: ')))

    for v in ficha:
        soma += v

    mos = input('Mostrar a situação [True/False]? ').capitalize().strip()
    if mos == 'True':
        sit = True

    else:
        sit = False

    ficha1['maior_nota'] = max(ficha)
    ficha1['menor_nota'] = min(ficha)
    ficha1['total'] = len(ficha)
    ficha1['média'] = soma / 4

    if ficha1['média'] > 7:
        situ = 'Aprovado'

    else:
        situ = 'Recuperação'

    if sit == True:
        ficha1['situção'] = situ

    print()
    for k, v in ficha1.items():
        print(f'{k} = {v}')

    return ficha1

notas()