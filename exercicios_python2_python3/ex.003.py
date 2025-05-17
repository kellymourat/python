radar= float(input('Digite a velocidade registrada: '))
if radar > 80:
    print (' Multado! excedeu 80km/km.')
    multa = (radar - 80) * 7
    print ('Total a pagar de multa € {:.2f}'.format(multa))
print('Tenha um bom dia, Seja prudente!')

