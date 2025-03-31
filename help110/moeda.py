def dobro(n = 0, f = False):
    res = n * 2 
    return res if f is False else moeda(res)

def metade(n = 0, f = False):
    res = n / 2
    return res if f is False else moeda(res)

def aumentar(n = 0, t = 0, f = False):
    res = ((n / 100) * t) + n
    return res if f is False else moeda(res)

def diminuir(n = 0, t = 0, f = False):
    res = n - (n * (t / 100)) 
    return res if f is False else moeda(res)

def moeda(n = 0):
    return 'R$' + f'{n:.2f}'.replace('.', ',')

def resumo(a, b, c):

    print('=' * 35)
    print('Resumo do valor'.center(35))
    print('-' * 35)

    print(f'Preço analisado: \t{moeda(a)}')
    print(f'Dobro do preço: \t{moeda(dobro(a))}')
    print(f'Metade do preço: \t{moeda(metade(a))}')
    print(f'{b}% de aumento: \t{moeda(aumentar(a, b))}')
    print(f'{c}% de diminuição: \t{moeda(diminuir(a, c))}')

    print('=' * 35)