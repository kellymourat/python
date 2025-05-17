casa= float(input('Valor da casa: € '))
sal= float(input('Digite o Valor salárial: € '))
anos= int(input('Em quantos anos pretende pagar ? '))
prestacao = casa / (anos * 12)
minimo = sal * 30 / 100
print('Para pagar uma casa de {:.2f}, em {} anos.'.format(casa,anos), end='')
print('Valor da mensalidade €{:.2f} por mês.'.format(prestacao))
if prestacao <= minimo:
   print ('Crédito CONCEDIDO!')
else:
    print('Crédito NEGADO!')
