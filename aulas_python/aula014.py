# estrutura de repetição while
# while é usado para quando não se sabe o limite

c = 0 # inicializa a variável 'c' com 0
while c < 10: 
    c += 1 # incrementa 'c' em 1 a cada iteração
    print(c)

valor = 1 # inicializa com um valor diferente de 0 para entrar em looping
par = impar = 0 #  inicializa com 0, pois a cada looping, adiciona 1

while valor != 0:
    valor = int(input(
        'Digite um valor: '
    ))
    if valor != 0:
        if valor % 2 == 0: # verifico se é par
            par += 1 # faço a contagem de números pares
        else:
            impar += 1 # faço a contagem de número ímpares

print(f'Você digitou {par} números pares e {impar} números ímpares.')


resposta_usuario = 'S' # inicializa 'S' para entrar em looping
while resposta_usuario == 'S': # continua enquanto o usuário digitar 'Ss', no caso True
    valor = int(input(
        'Digite um valor: '
    ))
    resposta_usuario = str(input(
        'Deseja continuar? [S/N]: '
    )).upper()

