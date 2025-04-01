# palindromo
frase = str(input('Digite uma frase qualquer: ')).replace(' ', '').strip()

# verificando se é um palíndromo
if frase[::-1] == frase:
    print(f'A frase {frase} é um Palíndromo.')
else:
    print(f'A frase {frase} não é um Palíndromo')
