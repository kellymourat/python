print('-='*18)
print('{:^35}'.format('Termos de uma PA'))
print('-='*18)
primeiro = int(input('Primeiro Termo: '))
razão = int(input('Segundo Termo: '))
termo= primeiro
cont=0
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
       print('{} -> '.format(termo),end='')
       termo += razão
       cont += 1
    print('Pausa')
    mais= int(input('Deseja saber mais termos ? '))
print('Total de termos foi {}'.format(total))