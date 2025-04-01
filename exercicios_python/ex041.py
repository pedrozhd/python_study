import datetime

ano = int(input('Digite o ano dem que você nasceu: '))
ida = datetime.date.today().year - ano

if ida <= 9:
    print('Você é um nadador MIRIM.')

elif ida > 9 and ida <=14:
    print('Você é um nadador INFANTIL.')

elif ida > 14 and ida <= 19:
    print('Você é um nadador JÚNIOR.')

elif ida > 19 and ida == 25:
    print('Você é um nadador SÊNIOR.')

elif ida > 25:
    print('Você é um nadador MASTER.')
