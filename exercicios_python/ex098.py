from time import sleep

def contador(a, b, c):
    print('-' * 50)
    print(f'Contagem de {a} até {b} pulando de {abs(c)} em {abs(c)}.')
    
    if c > 0:
        b += 1

    else:
        b -= 1

    for n in range(a, b, c):
        print(n, end=' -> ', flush=True)
        sleep(0.3)

    print('Fim!') 
    print('-' * 50)    


contador(1, 10, 1)
contador(10, 0, -2)

print()
print('Agora é sua vez de personalizar a contagem:')
a = int(input('ínicio: '))
b = int(input('Fim: '))
c = int(input('Passo: '))

if c == 0:
    print('Convertendo o 0 para o passo 1.')
    c = 1

if a > b and c > 0:
    c = -c

elif a < b and c < 0:
    c = abs(c)

if a == b:
    print('O começo e o fim não podem ser iguais.')

else:
    print()
    contador(a, b, c)