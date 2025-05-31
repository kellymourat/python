print('\033[35m''-='*10)
print('{:^30}'.format('\033[4;32m''»»» LOJAS KEL »»»''\033[m'))
print('\033[35m''-='*10, end='')
print('\033[m')
soma = cont = menor = tot = produto = 0
while True:
    p=str(input('Produto: ')).strip().upper()
    valor=float(input('Preço: € '))
    cont+=1
    soma+=valor
    if valor > 1000:
        tot += 1
    if cont == 1: # ou preço < menor:
        menor=valor
     #  produto = p
    else: # apaga esses comandos resolução do professor
        if  valor < menor:
              menor=valor
              produto=p
    c = ' '
    while c not in 'SN':
        c = str(input('Quer continuar ? [S/N] ')).strip().upper()
        print('\033[35m''«»'*15, end='')
        print('\033[m')
    if c != 'S':
       break
print('\033[31m'f'» Valor total da compra \033[32m {soma:.2f} euros.')
print('\033[31m'f'» Produto barato da loja: {produto} custa\033[32m € {menor:.2f}.')
print('\033[31m'f'» {tot} produtos custam mais de \033[32m € 1.000.''\033[m')
print('Origado, Volte SEMPRE! :)')
