print('='*40)
print('{:^40}'.format(' « BANCO PÉROLA » '))
print('='*40)
valor=int(input('Valor do saque: €'))
total = valor
céd = 500
totcéd = 0
while True:
    if total >= céd:
        total -= céd
        totcéd +=1
    else:
        if totcéd >0:
            print(f' Total {totcéd} Cédulas no valor €{céd}.')
        if céd == 500:
           céd = 200
        elif céd == 200:
             céd =100
        elif céd ==100:
             céd = 50
        elif céd ==50:
             céd =20
        elif céd ==20:
             céd = 10
        elif céd ==10:
             céd = 5
        elif céd ==5:
             céd = 1
        totcéd= 0
        if total == 0:
            break
print('Volte sempre! BANCO PÉROLA :)')



