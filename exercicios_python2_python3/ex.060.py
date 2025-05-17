n=int(input('Digite número para calcular seu factorial: '))
f=1
print('C... {}! ='.format(n),end='')
for c in range (n,0,-1):
    print(' {} '.format(c),end='')
    print(' x ' if c > 1 else '= ', end='')
    f*=c
print(f)

  
   

    n=int(input('Digite o número para calcular o seu factorial: '))
    c=n
    f=1
    print('Calculando {}! = '.format(n),end='')
    while c > 0:
        print('{}'.format(c),end='')
        print(' x ' if c > 1 else ' = ',end='')
        f *= c
        c-=1
    print('{}'.format(f))
    
  