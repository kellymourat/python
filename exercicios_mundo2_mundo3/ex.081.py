num = list()
while True:
    num.append(int(input('Digite um número: ')))
    resp = str(input(f'Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 10)
print(f'Total de números digitados {len(num)}')
num.sort(reverse=True)
print(f'Os valores em ordem decrecente {num}')
if 5 in num:
    print(
        f'Número 5 foi encrontrado na {num.index(5)}ª posição')  # code não funcionou, pois os valores estão em ordem decrescente.
else:
    print('O valor 5 não foi encontrado!')
