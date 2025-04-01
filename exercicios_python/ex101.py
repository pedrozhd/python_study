

def voto(ano):
    from datetime import date
    i = date.today().year - ano

    if i < 16:
        return f'Sua idade é {i} anos. Você não tem direito a voto.'

    elif 16 <= i < 18 or i > 65:
        return f'Sua idade é {i} anos. Seu voto é opcional.'

    else:
        return f'Sua idade é {i} anos. Seu voto é obrigatório.'


nasc = int(input('Ano de nascimento: '))
print(voto(nasc))