import datetime

ano = int(input('Em que ano você está? '))

if ano == 0:
    ano = datetime.date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano que você está, é bissexto. {ano}')
else:
    print(f'O ano em que você está, não é bissexto. {ano}')