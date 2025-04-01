# funções parte 2

'''
abertura e fechamento de parentêses indica uma função.
'''

# interactive help - help() ou .__doc__
# docstrings
# argumentos opcionais
# escopo de variáveis
# retorno de resultados
 
'''help'''
# help(print)
# print(input.__doc__)

'''docstrings'''
print()
def contador(i, f, p):
    """-> faz uma contagem e mostra na tela.

    Args:
        i (_type_): indica o ínicio
        f (_type_): fim da contagem
        p (_type_): passo da contagem
    função criada por pedrozhd
    """
    c = i
    while c <= f:
        print(f'{c} -> ', end='')
        c += p
    print('FIM!')
contador(2, 10, 2)
print()

'''argumentos opcionais'''
# caso o a, b ou c não receba nada, ele se torna o 0
def somar(a=0, b=0, c=0):
    s = a + b + c
    print(f'A soma vale {s}')

somar(3, 2, 5)
somar(b = 4, c = 2 )
somar(8, 4)
somar(6)
somar()
print()

'''escopo de variáveis'''
def teste():
    x = 8 # escopo local
    print(f'No programa teste, o n vale {n}')
    print(f'No programa teste, o x vale {x}')

# programa principal
n = 2 # escopo global
print(f'No programa principal o n vale {n}')
teste()
# print(f'No programa principal o x vale {x}')
print()


def teste1(b): # parâmetro formal
    global a # com esse comando o a global passar a valer o valor de a que está em local, no caso o 8
    a = 8 # aqui ele cria uma nova variável, só que apenas para o local, não altera o valor global de a
    b += 4
    c = 2
    print('Local')
    print(f'Aqui dentro(local) o a vale {a}') # escopo global, funciona dentro e fora da função
    print(f'Aqui dentro o b vale {b}') # escopo local, funciona apenas dentro da função
    print(f'Aqui dentro o c vale {c}') # escopo local, funciona apenas dentro da função

a = 5
teste1(a) # parâmetro real
print()
print('Global')
print(f'Aqui fora(global) o a vale {a}')
print()

'''retornando valores'''

def soma1(a=0, b=0, c=0):
    s = a + b + c
    return s

# quando retorna o s, o valor de s assume o lugar da variável
r1 = soma1(3, 2, 5) # aqui o s = 10 assumiu a variável r1, portanto r1 agora vale 10
r2 = soma1(2, 2)
r3 = soma1(6)

print(f'Os resultados foram {r1}, {r2} e {r3}')
print()

'''prática'''

def fatorial(n = 1):
    f = 1
    for c in range(n, 0, -1):
        f *= c
    return f

f1 = fatorial(5)
f2 = fatorial(2)
f3 = fatorial()
f4 = fatorial(int(input('Número: ')))

print(f'Os resultados são: {f1}, {f2}, {f3} e {f4}.')