n1 = float(input('Primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('Sua média escolar foi {}'.format(m))
if m >= 6.0:
    print('Parabéns você foi aprovado!')
else:
    print('Estude mais, não foi dessa vez!')

#print('Parabéns!' if m >=6.0 else ' Estude Mais!')
