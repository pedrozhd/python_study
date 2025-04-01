# deixei a string já em maiúsculo para facilitar a leitura do A, e tirei  os espaços dad bordas com STRIP
# usei a função replace para remover espaços no meio da string para fazer a contagem só com caracteres
fra = str(input('Digite um frase: ')).upper().strip().replace(' ', '')

# usei a função COUNT para contar quantas vezes a letra 'A' aparece no meu código
print(f"A letra 'A' aparece {fra.count('A')} vezes na sua frase!")

# usei a função FIND para encontrar aonde a letra 'A' aparece pela primeira vez, usei o +1 para anular a posição 0
print(f"A letra 'A' aparece pela primeira vez na posição {fra.find('A') + 1}")

# usei a função RFIND para encontrar aonde a letra 'A' aparece no último objeto da direita, +1 para anular a posição 0
print(f"a letra 'A' aparece pela última vez na posição: {fra.rfind('A') + 1}")