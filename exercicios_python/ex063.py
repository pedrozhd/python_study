# sequencia de fibonacci

quantidade_termos = int(input('Digite a quantidade de termos: '))

termo1 = 0
termo2 = 1

contador = 0

fibonacci_lista = []

while contador < quantidade_termos:
    fibonacci_lista.append(termo1)
    termo1, termo2 = termo2, termo1 + termo2
    contador += 1
print(' -> '.join(map(str, fibonacci_lista)), '-> Fim.')