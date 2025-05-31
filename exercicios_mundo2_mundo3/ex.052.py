num=int( input('Digite um número: '))
tot= 0
for c in range(1,num+1):
    if num % c ==0:
       print('\033[33m', end=' ')
       tot += 1
    else:
       print('\033[31m',end= ' ')
    print('{}'.format(c), end=' ')
print('\n\033[m''Número {} foi divisível {} vezes.'.format(num,tot))
if tot == 2:
    print('Número {} é primo!'.format(num))
else:
    print('Número {} não é primo!'.format(num))

# "número primo" refere-se a um número inteiro maior que 1 que só é divisível por 1 e por ele mesmo

