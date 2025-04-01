
def maior(*n):
    valores_validos = [valor for valor in n if valor !=0]

    print('Analisando os valores passados...')

    if valores_validos:
        print(f'{valores_validos} - Ao todo {len(valores_validos)} valores foram informados.')
        print(f'O maior valor informado foi: {max(valores_validos)}.')

    else:
        print('Nenhum valor válido foi informado (todos os valores foram 0).')

    print('-' *40)

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior(0)