# variáveis compostar (listas) parte 2
# as listas são mútaveis
# é possível dar append em listas usando a cópia de dados lista[:]

dados = list()
dados.append('Pedro')
dados.append(40)
# print(dados)

pessoas = list()
pessoas.append(dados[:]) # cópia

# dados[0] = 'Maria'
# dados[1] = 22

# pessoas.append(dados) # cria uma ligação, pois não está em formato de cópia
# print(pessoas) # dentro da lista, há uma lista, mas que é inalterável

dados[0] = 'Maria'
dados[1] = 22

pessoas.append(dados[:]) # cópia
print(pessoas)

galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera[0][0]) # executa a primeira sublista dentro da lista principal no índice 0

for pessoa in galera:
    print(f'{pessoa[0]} tem {pessoa[1]} anos de idade.')


galera1 = list()
dado = list()

for contador in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera1.append(dado[:])
    dado.clear()
print(galera1)


maior = menor = 0
for p in galera1:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        maior += 1
    else:
        print(f'{p[0]} é menor de idade.')
        menor += 1

print(f'{maior} pessoa(s) são maiores de idade.')
print(f'{menor} pessoa(s) são menores de idade.')