# análise de dados

quantidade_pessoas = 0
manipulacao = list()

maior_peso = float('-inf') # inicializa com o maior valor possível 
menor_peso = float('inf') # inicializa com o menor valor possível
pessoas_maior_peso = list()
pessoas_menor_peso = list()


while True:
    try:
        nome = str(input('Digite seu nome: '))
        peso = int(input('Digite seu peso: '))

        # adiciona os dados a lista de manipulação
        manipulacao.append([nome, peso])
        quantidade_pessoas += 1

        if peso > maior_peso:
            maior_peso = peso
            pessoas_maior_peso = [nome]

        elif peso == maior_peso:
            pessoas_maior_peso.append(nome)

        if peso < menor_peso:
            menor_peso = peso
            pessoas_menor_peso = [nome]

        elif peso == menor_peso:
            pessoas_menor_peso.append(nome)
        

        pergunta = str(input('Quer continuar? [S/N]: ')).upper().strip()
        if pergunta == 'N':
            break
            
    except ValueError:
        print('Comando Inválido.')

print(f'\nAo todo, {quantidade_pessoas} pessoas foram cadastradas.')
print(f'{maior_peso}KG é o maior peso e pertence a: {", ".join(pessoas_maior_peso)}.')
print(f'{menor_peso}KG é o menor peso e pertence a: {", ".join(pessoas_menor_peso)}.')
