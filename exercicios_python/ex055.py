
# lista para armazenar os pesos
lista_pesos = []
for c in range(1, 6):
    peso = float(input(f'Peso da {c}ª pessoa: ')) # entrada do peso
    lista_pesos.append(peso) # coloca as infos na lista

print(f'Maior peso: {max(lista_pesos):.2f}kg') # pega o maior número da lista
print(f'Menor peso: {min(lista_pesos):.2f}kg') # pega o menor número da lista