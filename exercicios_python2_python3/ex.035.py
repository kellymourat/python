sal=float(input('Qual é o valor salárial? €'))
if sal >= 1250:
     aument= sal + (sal * 10/100)
     print('Salários superiores ou igual €1250, terá um aumento 10%. Total a receber €{:.2f}'.format(aument))
else:
     aument= sal + ( sal * 15/100)
     print('Salários inferiores €1.250, terá um aumento 15% total a receber €{:.2f}'.format(aument))

