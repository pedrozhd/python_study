# funções

'''
São blocos nomeados de um código designado para fazer um trabalho em específico. Elas permitem que você escreva
o código uma vez que poderá ser usado a quantidade de vezes que você precisar para fazer uma mesma função. 

As funções podem pegar a informação que elas precisam e retornar a informação que elas geram. Então, basicamente
é um jeito de tornar os programas fáceis de escrever, ler, testar, e consertar.
'''

# função para quebrar a linha
def quebraLinha():
    print('\n')

# função para mostrar a formatação da linha
def mostraLinha():
    print('-' * 20)

# função para chamar o programa principal
def mostraTitulo(txt):
    mostraLinha()
    print(f'  {txt}')
    mostraLinha()

# o que está especificado em parentêses () vai entrar em (txt)
mostraTitulo('Sistema de Alunos')
mostraTitulo('Curso em Vídeo')
mostraTitulo('Pedro Henrique')

# chamando a função
quebraLinha()

def soma(a, b):
    s = a + b
    print(f'Resultado = {s}')

# programa principal
soma(4, 5)
soma(9, 8)
soma(2, 1)

quebraLinha()

# empacotamento em caso de tuplas
def contador(*n):
        tam = len(n)
        print(f'Recebi os valores {", ".join(map(str, n))} e são {tam} ao todo.') # converte o n em string

contador(2, 7, 1)
contador(8, 5, 4, 3)
contador(1, 5, 7, 9, 6)

quebraLinha()

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

# lista com os valores 
valores = [5, 6, 8, 4, 3]  

# valores entra no parâmetro de dobra, portanto lst passa a ser valores, logo tudo em lst altera em valores
dobra(valores)

# exibe os valores
print(valores)

quebraLinha()

def soma1(*valores):
    s = 0
    for n in valores:
        s += n
    print(f'Somando os valores, temos: {s}')

soma1(2, 4, 5, 6)
soma1(2, 5, 4)