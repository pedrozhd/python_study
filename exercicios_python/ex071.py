# caixa 

while True:
    try:
        # entrada de saque
        saque_dinheiro = int(input('Você deseja sacar quanto? '))
        if saque_dinheiro < 1:
            print('Comando Inválido. O mínimo de saque é R$1,00')
        else:
            break # sai do loop se for válido
    except ValueError:
        print('Entrada Inválida. Digite apenas números.')
    

# vou tirando do caixa até zerar
total_caixa = saque_dinheiro

# inicio com a maior cédula
cedula = 50

# contador de cédulas
cont_cedulas = 0


while True:

    # verifico se o valor total em caixa é maior ou igual a 50
    if total_caixa >= cedula:
        total_caixa -= cedula
        cont_cedulas += 1
    else:

        # exibe se pelo menos uma cédula foi usada
        if cont_cedulas > 0:
            print(f'Total de {cont_cedulas} cédulas de R${cedula}')

        # não conseguiu tirar 50 do total, logo há menos do que 50 para receber
        if cedula == 50:
            cedula = 20

        # não conseguiu tirar 20 do total, logo há menos de 20 para receber
        elif cedula == 20:
            cedula = 10

        # não conseguiu tirar 10 do total, logo há menos de 10 para receber
        elif cedula == 10:
            cedula = 1
        
        cont_cedulas = 0 # zera o contador para cada nova cédula

        # quando o dinheiro em caixa acabar, o programa encerra
        if total_caixa == 0:
            break
