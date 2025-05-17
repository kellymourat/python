# professor 
from random import randint
computador= randint(0,10)
print('\033[36m' '»»»»» Sou o computador vou pensar em um número entre 0 e 10. Tente adivinhar! »»»»»»''\033[m')
acertou= False
palpites= 0
while not acertou:
    jogador=int(input('Digite o seu palpite: '))
    palpites += 1
    if jogador == computador:
        acertou= True
    else:
        if jogador < computador:
            print('\033[0;31m''Mais... jogue novamente!''\033[m')
        elif jogador > computador:
            print('\033[0;31m''Menos... jogue novamente!''\033[m')
print('Computador pensou no {}'.format(computador))
print('Acertou com {} tentativas. Parabéns!!!'.format(palpites))


# Kelly
'''from random import randint
computador= randint(0,10)
print(' »»»»»»»» Tenta adivinhar, um número entre 0 e 10 »»»»»»»» ')
cont=0
jogador=''
while jogador != computador:
    jogador = int(input('Adivinhe o número: '))
    cont+=1
    if computador == jogador:
      print('Parabéns Jogador venceu com {} tentativas!!!'.format(cont))
    else:
       if jogador < computador:
         print('\033[0;31m''Mais.. tente novamente''\n033[m')
       elif jogador > computador:
         print('\033[0;31m''Menos... Jogue novamente!''\033[m')
print('Computador escolheu {}!'.format(computador))'''





