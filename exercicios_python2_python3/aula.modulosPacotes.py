def fatorial(n):
    f = 1
    for c in range(1, n + 1):
        f *= c
    return f


num = int(input('digite um número: '))
fat = fatorial(num)
print(f'Fatorial de {num} é {fat}')
