
soma = 0
contador = 0
numeros_lista = []

while True:
    num = int(input('Digite um número: '))
    numeros_lista.append(num)
    contador += 1
    soma += num
    media = soma / contador

    pergunta = str(input('Quer continuar? [S/N] ')).strip().upper()
    if pergunta == 'N':
        break

print(
    f'Esse foi o maior número digitado: {max(numeros_lista)}.\n'
    f'Esse foi o menor número digitado: {min(numeros_lista)}.\n'
    f'Essa foi a média entre os números: {media:.2f}' 
)