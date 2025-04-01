# número por extenso

nomes = (
    'zero', 
    'um', 
    'dois', 
    'três', 
    'quatro', 
    'cinco', 
    'seis', 
    'sete',
    'oito',
    'nove',
    'dez',
    'onze',
    'doze',
    'treze',
    'catorze',
    'quinze',
    'desesseis',
    'desessete',
    'dezoito',
    'dezenove',
    'vinte'
)
    
while True:
    try:
        numero = int(input('Digite um número entre 0 e 20: '))
        if numero > 20 or numero < 0:
            print('Tente um número entre 0 e 20.')
        else:
            break
    except ValueError:
        print('Comando Inválido!')

print(f'Você digitou o número {(nomes[numero])}.')
