import datetime


maior_idade = 0
for c in range(1, 8):
    ano_nascimento = int(input(f'Ano de nascimento da {c}ª pessoa: ')) # comando para repetir 7 vezes
    idade = datetime.date.today().year - ano_nascimento # verificando a idade
    if idade >= 18:
        maior_idade += 1 # soma das pessoas adultas

print(f'{maior_idade} pessoas são maiores de idade.')
print(f'{7 - maior_idade} pessoas são menores de idade.')

