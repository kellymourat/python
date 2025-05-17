nota1= float(input('Digite primeira nota: '))
nota2= float(input('Digite segunda nota: '))
média= (nota1 + nota2) / 2
print('Analisando 1ª nota {}, 2ª nota {}. Sua média {}.'.format(nota1,nota2,média))
if média < 5.0:
    print('Sua média ficou abaixo 5.0 REPROVADO!')
elif média >=5 and média < 7:
# 7 > média >= 5:
    print('Sua média ficou entre 5.0 e 6.9, estude mais está de RECUPERAÇÃO!')
elif média >= 7.0:
    print('Parabéns você foi aprovado!')

