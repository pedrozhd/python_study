# leitura

contador_idade = 0
contador_homens = 0
contador_menos20 = 0

while True:
    # validação do sexo
    # não é necessário o uso do try-except, porque o programa continua rodando mesmo com o erro.
    while True:
        sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()
        if sexo in ['M', 'F']:
            break
        print('Entrada Inválida.')

    # validação da idade
    while True:
        try: # o uso do try acontece se o usuário digitar algo diferente de um número e o programa dar um ValueError.
            idade = int(input('Informe a sua idade: '))
            break
        except ValueError: # se houver erro, o programa capta e exibe a mensagem, impedindo o fechamento.
            print('Insira apenas números.')

    # validação da pergunta
    # não é necessário o uso do try-except, porque o programa continua rodando mesmo com o erro.
    while True:
        pergunta = str(input('Quer continuar cadastrando pessoas [S/N]? ')).strip().upper()
        if pergunta in ['S', 'N']:
            break
        print('Entrada Inválida! Tente S ou N.')

    # contagem das estatísticas
    if idade > 18:
        contador_idade += 1

    if sexo == 'M':
        contador_homens += 1

    if sexo == 'F' and idade < 20:
        contador_menos20 += 1

    if pergunta == 'N':
        break

print(f'Ao todo {contador_idade} pessoa(s) tem mais de 18 anos.')
print(f'Ao todo foram registrados {contador_homens} homen(s).')
print(f'Ao todo foram registrado {contador_menos20} mulher(es) com menos de 20 anos.')
print('Fim do Programa.')
    