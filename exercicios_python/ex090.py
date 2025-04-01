# aprovado ou reprovado

info = dict()

while True:
    try:
        info['Nome'] = input('Digite seu nome: ').capitalize()
        info['Média'] = float(input(f'Média do {info['Nome']}: '))

        if info['Média'] < 7:
            info['Situação'] = 'Reprovado'
        else:
            info['Situação'] = 'Aprovado'

        for k, v in info.items():
            print(f'{k} é igual a {v}')
        print('-' * 30)
        break
    
    except ValueError:
        print('Comando Inválido.')
        print('\n' + '=' * 30)
