def dobro(n = 0):
    return n * 2

def metade(n = 0):
    return n / 2

def aumentar(n = 0, t = 0):
    res = ((n / 100) * t) + n
    return res

def diminuir(n = 0, t = 0):
    res = n - (n * (t / 100)) 
    return res