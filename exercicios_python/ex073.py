# estatística

tabela_brasileirao = (
    'Botafogo',
    'Palmeiras',
    'Flamengo',
    'Fortaleza',
    'Internacional',
    'São Paulo',
    'Corinthians',
    'Bahia',
    'Cruzeiro',
    'Vasco da Gama',
    'EC Vitória',
    'Atlético-MG',
    'Fluminense',
    'Grêmio',
    'Juventude',
    'Bragantino',
    'Athletico-PR',
    'Criciúma',
    'Atlético-GO',
    'Cuiabá'
)

print('Aqui está os 5 primeiros colocados:')
for c in tabela_brasileirao[:5]:
    print(c)

print('-=' * 30)

print('Aqui está os 4 últimos colocados:')
for c in tabela_brasileirao[16:]:
    print(c)

print('-=' * 30)

print('Aqui está a tabela em ordem:')
for c in sorted(tabela_brasileirao):
    print(c)

print('-=' * 30)

print(f'O time do Vitória está na {tabela_brasileirao.index('EC Vitória')}º posição!')