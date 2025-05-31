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
