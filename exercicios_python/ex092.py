# cadastro
import datetime

cad = dict()

while True:
    cad['nome'] = input('Digite seu nome: ')
    nasc = int(input('Ano de nascimento: '))
    cad['idade'] = datetime.date.today().year - nasc

    cad['ctps'] = int(input('Digite o número da sua carteira de trabalho (0 interrompe): '))

    if cad['ctps'] == 0:
        print('\nEssas são as sua informações.')
        for k, v in cad.items():
            print(f'{k} = {v}')
        break

    cad['ano de contratação'] = int(input('Informe o ano de contratação: '))
    cad['salário'] = float(input('Informe o salário: '))
    cad['tempo de contribuição'] = (datetime.date.today().year - cad['ano de contratação'])

    idade_minima = 65
    tempo_minimo_contribuido = 35

    if cad['tempo de contribuição'] >= tempo_minimo_contribuido and cad['idade'] >= idade_minima:
        cad['idade de aposentadoria'] = cad['idade']

    else:
        anos_faltantes_tempo = max(tempo_minimo_contribuido - cad['tempo de contribuição'], 0)
        anos_faltante_idade = max(idade_minima - cad['idade'], 0)
        anos_faltantes = max(anos_faltantes_tempo, anos_faltante_idade)
        cad['idade de aposentadoria'] = cad['idade'] + ((cad['ano de contratação'] + 35) - datetime.date.today().year)
    print('\nInformações cadastradas.')
    for k, v in cad.items():
        print(f'{k} = {v}')

    break