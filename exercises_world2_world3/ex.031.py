distância= float(input('Qual a distância da sua viagem? '))
print('Viagem pretendida {}km, Calculando preço da sua passagem.'.format(distância))
if distância <= 200:
    preco= distância * 0.50
    print('Valor calculado para viagens até 200km €{:.2f}'.format(preco))
else:
    preco = distância * 0.45
    print('Viagens longas acima de 200km: Total a pagar €{:.2f}'.format(preco))

# preço= distância * 0.45 if distância <=200 else distância * 0.45
# print('Calculando valor... total de {}'.format(preço))





