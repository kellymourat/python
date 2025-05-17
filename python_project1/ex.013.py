dias= int(input('Dias alugados:'))
km= float(input('Total de km:'))
pago = (dias * 60 ) + (km * 0.15)
print('Total a pagar: R${:.2f}'.format(pago))