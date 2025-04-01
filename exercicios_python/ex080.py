
valores = list()

for i in range(5):
    num = (int(input('Digite um número: ')))
    
    # se a lista estiver vazia adiciona
    if not valores or num > valores[-1]: # se num for maior que o último, ele deve ir para o final
        valores.append(num)

    else:
        for posicao in range(len(valores)): # percorrre a lista para achar a posição correta
            if num <= valores[posicao]: # se o número for menor ou igual ao da posição
                valores.insert(posicao, num) # insere na posição correta
                break

print(f'Lista ordenada: {valores}')