# leitor de mercadoria

gasto = 0
contador_1000 = 0
mais_barato = ''
menor_preço = float('inf') # número infinito positvo

while True:
    nome =  str(input('Digite o nome do produto: '))

    # validação do preço
    while True:
        try: 
            valor = float(input('Digite o preço do produto: R$'))
            gasto += valor
            break
        except ValueError:
            print('Insira somente números.')

    if valor < menor_preço:
        menor_preço = valor
        mais_barato = nome

    # contagem de produtos aciama de R$1000,00
    if valor > 1000:
        contador_1000 += 1

    # validação de resposta
    while True:
        pergunta = str(input('Quer continuar cadastrando [S/N]? ')).upper().strip()
        if pergunta in ['S', 'N']:
            break
        print('Entrada Inválida. Tente S ou N.')

    if pergunta == 'N':
        break

print(f'A soma dos valores é igual a: R${gasto:.2f}.')
print(f'{contador_1000} produto(s) custa(m) mais de R$1000,00.')
print(f'O produto mais barato custa R${menor_preço:.2f} e o seu nome é {mais_barato}!')