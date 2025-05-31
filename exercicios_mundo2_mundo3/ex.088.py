from random import randint
from time import sleep

lista = list()
jogos = list()
print('-=' * 20)
print('{:^35}'.format('MEGA SENA'))
print('-=' * 20)
quant = int(input('Quantos jogos você quer que eu sortei ? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('»' * 6, f'< SORTEANDO {quant} JOGOS >', '»' * 6)
for i, l in enumerate(jogos):
    print(f' jogo {i + 1}: {l}')
    sleep(1)
print('»' * 10, '< BOA SORTE >', '»' * 10)
