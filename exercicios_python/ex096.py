def lin():
    print('-' * 20)

def titulo(txt):
    print(txt)
    lin()
titulo('Controle de Terreno!')

def area(a, b):
    s = a * b
    lin()
    print(f'Altura = {a}m² \nLargura = {b}m² \nÁrea = {s:.2f}m²')

alt = float(input('Altura do terreno: '))
lar = float(input('Comprimento do terreno: '))
area(alt, lar)