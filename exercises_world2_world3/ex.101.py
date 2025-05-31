def lin():  
    print('_' * 30)


def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade <= 16:
        return f'Com {idade} anos de idade, VOTO NEGADO!'
    elif idade <= 65:
        return f'Com {idade} anos de idade, VOTO OBRIGATÓRIO!'
    else:
        return f'Com {idade} anos anos de idade, VOTO OPCIONAL!'


lin()
nasc = int(input('Em que ano você nasceu ? '))
print(voto(nasc))
