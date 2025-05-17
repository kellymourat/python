matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = ster = maisegl = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite número [{l},{c}]: '))
print('{:^25}'.format('«»«»«» Matrizzz «»«»«»'))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()
for c in range(0, 3): 
    ster += matriz[c][2]
print(f'Soma dos valores PARES: {spar}')
print(f'Soma da terceira coluna: {ster}')
for l in range(0, 3): 
    if l == 0:
        maisegl = matriz[l][2]
    if matriz[l][2] > maisegl:
        maisegl = matriz[l][2]
print(f'O maior número da segunda linha: {maisegl}')

# Resolução kelly :)