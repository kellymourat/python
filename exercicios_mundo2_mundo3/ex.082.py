num = list()
pares = list()
impares = list()
while True:
    num.append(int(input('Digite um número: ')))
    r = str(input('Quer continuar ? [S/N] '))
    if r in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    else:
        if v % 2 == 1:
            impares.append(v)
print(f'Lista completa é: {num}')
print(f'Valores PARES da lista: {pares}')
print(f'Valores ÍMPARES da lista: {impares}')
