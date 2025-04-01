import datetime

ano = int(input('Digite o ano em que você nasceu: '))
ida = datetime.date.today().year - ano

if ida < 18:
    print(f'Você ainda vai se alistar ao exército, falta {18 - ida} ano(s).')

elif ida == 18:
    print(f'Você deve se alistar! Já está com {ida} anos.')

else:
    print(f'Você está atrasado há {ida - 18} ano(s).')

