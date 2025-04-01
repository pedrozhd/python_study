r1 = float(input('Digite o comprimento do primeiro segmento: '))
r2 = float(input('Digite o comprimento do segundo segmento: '))
r3 =  float(input('Digite o comprimento do terceiro segmento: '))

if r1 == r2 == r3:
    print('Você tem um triângulo equilátero. Formado por 3 lados iguais.')

elif r1 == r2 != r3 or r2 == r3 != r1 or r3 == r1 != r2:
    print('Você tem um triângulo isóceles. Formado por 2 lados iguais.')

elif r1 != r2 != r3:
    print('Você tem um triângulo escaleno. Formado por 3 lados distintos.')