print('{:»^50}'.format(' Vamos Jogar PAR / IMPAR '))
from random import randint
v=0
while True:
    jogador=int(input('jogue um número: '))
    computador=randint(1,10)
    total= jogador + computador
    tipo= ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]
    print('='*30)
    print(f'Computador Jogou: {computador} \nJogador Jogou: {jogador} \n A soma entre os números foi {total}', end='')
    print(' DEU PAR' if total % 2 == 0 else ' DEU ÍMPAR')
    print('='*30)
    if tipo == 'P':
       if total % 2 == 0:
            print('»'*15)
            print('JOGADOR VENCEU!')
            v+=1
       else:
           print('»'*15)
           print('JOGADOR PERDEU!')
           break
    elif tipo == 'I':
        if total % 2 ==1:
            print('»'*15)
            print('JOGADOR VENCEU!')
            v+=1
        else:
           print('»'*15)
           print('Você PERDEU!!')
           break
    print('Vamos jogar Novamente ? ')
print('»'*15)
print(f'GAME OUVER!!! total de vitórias {v}')
