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