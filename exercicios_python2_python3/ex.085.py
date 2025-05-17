lista = [[], []]
num = 0
for c in range(1, 8):
    num = int(input(f'Digite o {c} número: '))
    if num % 2 == 0:
        lista[0].append(num)
    elif num % 2 == 1:
        lista[1].append(num)
print('»' * 35)
lista[0].sort()
lista[1].sort()
print(f'Lista com números PARES: {lista[0]}')
print(f'Lista com números Ímpares: {lista[1]}')
