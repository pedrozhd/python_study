# melhorando 

print('Gerador de P.A')
print('-=' * 20)

# recebe o valor do primeiro termo
primeiro_termo = int(input(
    'Digite o primeiro termo: '
))

# recebe o valor da razão
razao = int(input(
    'Digite a razão da progressão: '
))

# o termo recebe o primeiro termo da progressão
termo = primeiro_termo

# começa em 1 para contar os termos
contador = 1

# crio uma variável lista que vai armazenar o termos
pa_lista = []

# enquanto o contador não chegar no décimo termo o programa não para
while contador <= 10:
    print(f'{termo} -> ', end= '')
    pa_lista.append(termo)
    termo += razao # a cada looping o termo recebe o termo + razão (é o próximo termo)
    contador += 1 # após cada looping adiciona-se 1 um termo no contador até chegar a dez

print('Pausa.')
print('-=' * 20)

termo1 = pa_lista[-1] # o termo1 é o último termo da lista 
termo2 = termo1 + razao # é o próximo termo após o último termo da lista

while True:

    # pergunto a quantidade de termo a ser adicionado
    novo_termo = int(input('Deseja adicionar mais quantos termos? '))

    # caso for 0, o programa já encerra
    if novo_termo == 0:
        break

    print('-=' * 20)

    contador1 = 1
    while contador1 <= novo_termo:
        print(f'{termo2} -> ', end= '')
        termo2 += razao
        contador += 1
        contador1 += 1

    print('Pausa.')
    print('-=' * 20)
print(f'Fim do Programa. Houve {contador - 1} termos mostrados.')