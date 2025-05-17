def fatorial(n, show=False):
    """
    -> Calculando número de fatorial
    :param n: O número a ser calculado
    :param show: (opcional) Mostra ou não a conta
    :return: O valor do Fatorial de um número n.
    """
    f = 1
    for c in range(n, 0, -1):
        f *= c
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' =', end=' ')
    return f


n = int(input('Fatorial: '))
print(fatorial(n, show=True))
# help(fatorial)
