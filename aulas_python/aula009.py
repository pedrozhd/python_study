# manipulação de texto

frase = 'Curso em Vídeo Python' # o índice se inicia no 0

# fatiamento --> pegar pedaços de um string
print(frase[9]) # --> pega apenas o de índice 9, no caso o V

print(frase[9:14]) # pega a cadeia do índice 9 ao 13, pois excluí-se o último 

print(frase[9:21]) # vai parar no 20 como propriamente dito anteriormente

print(frase[9:21:2]) # do índice 9 ao 21 pulando de 2 em 2
 
print(frase[:5]) # começa do ínicio

print(frase[6:]) # começa no caractere 5 e vai até o final

print(frase[9::3]) # começa no 9 e vai até o final pulando de 3 em 3

print('-' * 20)

# análise --> análise de um string, quantas letras? termina com qual? começa com qual?
print(len(frase)) # --> conta quantas caracteres tem a frase

print(frase.count('o')) # conta quantas vezes a letra dentro do espaço apareceu

print(frase.count('o', 0, 14)) # contagem com fatiamento

print(frase.find('deo')) # onde ele encontrou a primeira letra da palavra/frase/letra na string

print('Curso' in frase) # diz se há a presença do objeto

print('-' * 20)

# transformação
print(frase.replace('Python', 'Iphone')) # faz a procura da string e substitui a mesma

print(frase.upper()) # deixa tudo em maiúsculo

print(frase.lower()) # deixa tudo em minúsculo

print(frase.capitalize()) # só o primeiro caractere em maiúsculo

print(frase.title()) # deixa toda palavra da frase com a primeira letra maiúscula

frase2 = '   Aprenda Python  '

print(frase2.strip()) # remove espaços desnecessários da string

print(frase2.rstrip()) # remove espaços a direita da string

print(frase2.lstrip()) # remove os espaços a esquerda da string

print('-' * 20)

# divisão

print(frase.split()) # divisão considerando os espaços entre as palavras na string, criando novos índices
print(frase.split()[0]) # pega a palavra da lista no índice 0, no caso 'Curso'
print(frase.split()[0][3]) # mostra a letra 3 dentro do índice 0

print('-'.join()) # junta todos os elementos da frase