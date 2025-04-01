
def ajuda(com):
    help(com)

def titulo(msg, cor=0):
    tam = len(msg)
    print('~' * tam)
    print(msg)
    print('~' * tam)


comando = ''

while True:
    titulo('Sistema de Ajuda PyHelp.')
    comando = input('Função ou biblioteca: ')
    if comando.upper() == 'FIM':
        break

    else:
        ajuda(comando)