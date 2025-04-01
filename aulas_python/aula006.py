# tipos primitivos

# int (números inteiros) 13 - 05 - 2023
# float (números com vírgula/ponto) 1.3 - 0.5 - 20,23
# bool (True, False) - and, or, not
# str (dado que armazena texto) 'pedro', 'oi', '' --> string vazia

n1 = (input('Número: '))

# tipo da classe
print(type(n1))

n2 = int(input('Número: '))

print(type(n2))

s = n1 + n2

print(f'a soma entre {n1} e {n2} vale {s}')

print(n1.isnumeric()) # a variável tem que ser uma str
print(n1.isalpha()) # ver se é letra
print(n1.isalnum()) # ver se é alfanúmerico