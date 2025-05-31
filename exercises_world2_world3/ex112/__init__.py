def aumentar(n=0, percentual=10, formato=False):
    """
        — > função para analisar moedas e fortamar valores
       :param n: valor a ser analisado
       :param replace: valor a ser formatado remove o ponto
       :return formato=False: Ao usar formato=True converter o valor em moeda com casa decimal
       """
    resp = n + (n * percentual / 100)
    return resp if formato is False else moeda(resp)


def diminuir(n=0, percentual=10, formato=False):
    resp = n - (n * percentual / 100)
    return resp if formato is False else moeda(resp)


def dobro(n=0, formato=False):
    resp = n * 2
    return resp if formato is False else moeda(resp)


def metade(n=0, formato=False):
    resp = n / 2
    return resp if formato is False else moeda(resp)


def moeda(n=0, moeda='R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')


def resumo(n=0, taxaa=10, taxar=5):
    print('_' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('_' * 30)
    print(f'Valor analisado: \t{moeda(n)}')
    print(f'Dobro do valor:   \t{dobro(n, True)}')
    print(f'Metade do valor:   \t{metade(n, True)}')
    print(f'{taxaa}% de aumento :  \t{aumentar(n, taxaa, True)}')
    print(f'{taxar}% redução:       \t{diminuir(n, taxar, True)}')
    print('_' * 30)
