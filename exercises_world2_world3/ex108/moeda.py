def aumentar(n=0):
    return n + (n * 10 / 100)



def dobro(n=0):
    return n * 2


def metade(n=0):
    return n / 2


def moeda(n=0, moeda='R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')


# def diminuir(preço):
# res= preço( preço * 10/100)
# return res
