# entrada do preço do produto
preco_produto = float(input('Insira o preço do produto: R$'))

# opção de pagamentos
opcao_pagamento = int(input(
    'Escolha a opção: \n'
    'À vista. Dinheiro/Cheque --> 1 \n'
    'À vista. Cartão --> 2 \n'
    'Parcelado 2x. --> 3 \n'
    'Parcelado 3x ou mais. --> 4 \n'
    'Digite a opção: '
))

# calculo do preço final de acordo com a opção escolhida
if opcao_pagamento == 1:
    preco_final = preco_produto - (preco_produto * (10/100)) # 10% de desconto
    print('Dada a opção 1:') 
    print('Você recebeu 10% de desconto.')
    print(f'Preço final do produto: R${preco_final:.2f}')

elif opcao_pagamento == 2:
    preco_final = preco_produto - (preco_produto * (5/100)) # 5% de desconto
    print('Dada a opção 2:') 
    print('Você recebeu 5% de desconto.')
    print(f'Preço final do produto: R${preco_final:.2f}')

elif opcao_pagamento == 3:
    preco_final = preco_produto
    valor_parcela = preco_produto / 2
    print('Dada a opção 3:')
    print('Seu produto foi parcelado em 2x')
    print(f'Valor de cada parcela: R${valor_parcela:.2f}')
    print(f'O preço final do seu produto é de R${preco_final:.2f}.')

elif opcao_pagamento == 4:
    parcelas = int(input('Escolha o número de parcelas (Minímo 3): '))

    # garante que o usuário escolha pelo menos 3 parcelas
    if parcelas < 3:
        print('Opção inválida. Escolha pelo menos 3 parcelas.')
    
    else:
        preco_final = preco_produto * (1 + 0.20) # 20% de juros
        valor_parcela = preco_final / parcelas
        print('Dada a opção 4:')
        print(f'Número de parcelas: {parcelas}x com 20% de juros.')
        print(f'Valor de cada parcela: R${valor_parcela:.2f}')
        print(f'Valor total: R${preco_final:.2f}')

else:
    print('Opção inválida. Escolha uma opção entre 1 e 4.')