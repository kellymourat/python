peso= float(input('Qual é o seu peso ? (Kg) '))
altura= float(input ('Qual é a sua altura ? (m) '))
imc= peso / ( altura ** 2)
print('O imc dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Abaixo do peso!')
elif 18.5 <= imc < 25:
    print('Peso Ideal!')
elif 25 <= imc < 30:
    print('SOBREPESO!')
elif 30 <= imc < 40:
    print('OBSIDADE!')
else:
    print('OBSIDADE MÓRBIDA!')

# elif média >= 5 and média < 7:
# 7 > média >= 5: