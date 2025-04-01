# módulos e pacotes
# ínicio na década de 60
# sistemas ficando cada vez maiores

# foco:
# - dividir um programa grande
# - aumentar a legibilidade
# - facilitar a manutenção

# módulos
'''
módulo é onde se guarda coisas úteis como funções de um nicho específico, ex: números.
'''
import aula022u

num = int(input('Digite um número: '))
fat = aula022u.fatorial(num)

print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {aula022u.dobro(num)}')

# pacotes
'''
pacotes é onde se guarda diversas funções que são nomeadas de diferentes maneiras, a fim de facilitar.
'''

from utilitários import números

num = int(input('Digite um número: '))
fat = aula022u.fatorial(num)

print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {números.dobro(num)}')
