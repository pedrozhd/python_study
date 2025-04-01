# verificação M ou F

sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]

while sexo not in 'MF':
    print('Comando Inválido!')
    sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]
print('Obrigado.')