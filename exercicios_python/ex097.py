
def escreva(txt):
    print('~' * (len(txt) + 2))
    print(txt.center(len(txt) + 2))
    print('~' * (len(txt) + 2))
    print()


escreva(input('Digite algo: '))
escreva('Pedro Henrique')
escreva('Curso em Vídeo')
escreva('Python')