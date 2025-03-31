def leiaDinheiro(msg):
    v = False
    
    while not v:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print('Preço inválido.')

        else:
            v = True
            return float(entrada)