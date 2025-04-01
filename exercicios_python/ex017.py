from math import sqrt, hypot
ca = float(input('Digite o comprimento do cateto adjacente: '))
co = float(input('Digite o comprimento do cateto oposto: '))
hip = sqrt(ca ** 2 + co ** 2) 

# ou

hi = hypot(ca, co) # --> função de hipotenusa

print(f'Com o C.A valendp {ca} e o C.O valendo {co}, sua HIP é: {hip:.2f}')