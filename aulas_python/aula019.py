# dicionários
# estruturas semelhante as listas e tuplas, mas com índices literais (nome, número, etc)
# são exibidos por chaves {}
# não se usa append

dados = dict()
dados = {'nome':'Pedro', 'idade': 25}
dados['nome'] = 'Leandro' # são mutáveis
print(dados['nome'])
print(dados['idade'])

# para adicionar algo ao dicionário, usaremos:
dados['sexo'] = 'M'
print(dados['sexo'])

# remover elementos
del(dados['idade'])

print('\n')
filme = {'título':'StarWars',
         'ano':'1977',
         'diretor':'George Lucas'
        }

print(filme.values()) # me retorna todos os valores, sem retornar as keys
print(filme.keys()) # me retorna a atribuição, ex: titulo, ano e diretor
print(filme.items()) # me retorna ambos
print(f'O filme {filme["título"]} foi a público em {filme["ano"]}.')
print('\n')

for keys in filme.keys():
    print(keys)
print('\n')

for values in filme.values():
    print(values)
print('\n')

# basicamente o enumerate: posição e valor
for keys, values in filme.items():
    print(f'{keys} = {values}')

# posso utilizar dicionários + listas
print('\n')
locadora = list()
locadora.append(filme) # isso vai se tornar o primeiro índice, no caso o 0

print(locadora[0]['ano'])
print('\n')

estados = list()
estado1 = {'uf': 'Minas Gerais', 'sigla': 'MG'}
estado2 = {'uf': 'Bahia', 'sigla': 'BA'}
estados.append(estado1)
estados.append(estado2)

print(estados[0]['uf'])
print('\n')

states = dict()
brasil = list()
for c in range(0, 3):
    states['uf'] = input('Unidade Federativa: ').capitalize()
    states['sg'] = input('Sigla: ').upper()
    brasil.append(states.copy()) # comando interno dos dicts

for e in brasil:
    for keys, values in e.items():
        print(f'{keys} = {values}')
 
for e in brasil:
    for values in e.values():
        print(f'{values}', end=' ')
    print()