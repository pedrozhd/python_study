

def fatorial(n, show=False):
    f = 1
    for c in range(n, 0, -1):

        if show:
            print(c, end='')

            if c > 1:
                print(f' x ', end='')

            else:
                print(' = ', end='')
        f *= c
    return f

# verificação
mostrar = input('Mostrar [True/False]? ').capitalize().strip()
if mostrar == 'True':
    show = True

else:
    show = False

print(fatorial(int(input('Número: ')), show))