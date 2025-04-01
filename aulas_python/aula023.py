# tratamento de erros

try: # tenta executar

    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite outro: '))
    di = n1 / n2

except (TypeError, ValueError):
    print('Tivemos um problema com os tipos de dados que você digitou.')

except ZeroDivisionError:
    print('Não é possível dividir um número por 0.')

except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados.')
    
# except Exception as error: # em caso de erro, imprime:
    # print(f'Infelizmente tivemos um problema, o prolema occorreu devido: {error.__class__}!')

else: # ocorre se der certo
    print(f'O resultado é: {di}')

finally: # acontece independente da falha
    print('Volte sempre!')
