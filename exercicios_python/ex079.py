
valores = list()

while True:
    try:
        numero = int(input('Digite um número: '))

        if numero not in valores:
            valores.append(numero)
            print('Número adicionado.')

        else:
            print('Esse número já foi adicionado.')

        while True:
            pergunta = str(input('Quer continuar [S/N]? ')).upper().strip()
            if pergunta in ('S', 'N'):
                break
            print('Entrada Inválida.')

        if pergunta == 'N':
            break

    except ValueError:
        print('Comando Inválido.')

print('-=' * 35)
# map(função, sequência) aplica a função a cada elemento da sequência.
# no caso, map(str, ...) converte todos os números para strings, porque join() só funciona com strings.

print(f'Aqui está todos os valores digitados, exceto repetidos: {", ".join(map(str, sorted(valores)))}.')

# join() junta todos os elementos de um iterável (lista, tupla, etc.) em uma única string.
# Cada elemento é separado pelo que está antes do .join() (nesse caso, ", " que adiciona uma vírgula e um espaço).

