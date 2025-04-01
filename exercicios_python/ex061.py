# p.a usando while

print('Gerador de P.A')
print('-=' * 12)

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

# enquanto o contador não chegar no décimo termo o programa não para
while contador <= 10:
    print(f'{termo} -> ', end= '')
    termo += razao # a cada looping o termo recebe o termo + razão (é o próximo termo)
    contador += 1 # após cada looping adiciona-se 1 um termo no contador até chegar a dez
print('Fim.')