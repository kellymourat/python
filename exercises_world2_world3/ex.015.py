from random import randint
from time import sleep
itens = ['Pedra',' Papel','Tesoura']
computador= randint(0, 2)
print('{:»^60}'.format(' JOKENPÔ '))
print('''Escolha uma opção
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador= int(input('Sua jogada ? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
print('»«'*15)
print('Computador jogou {}'.format(itens[computador]))
print('jogador jogou {}'.format(itens[jogador]))
print('»«'*15)
if computador ==0:
   if jogador ==0:
       print('EMPATE!')
   elif jogador ==1:
       print('JOGADOR VENCEU!')
   elif jogador ==2:
       print('COMPUTADOR VENCEU!')
   else:
       print('\033[0;31m''JOGO INVÁLIDO!')

elif computador ==1:
   if jogador ==0:
       print('COMPUTADOR VENCEU!')
   elif jogador ==1:
       print('EMPATE!')
   elif jogador ==2:
     print('JOGADOR VENCEU!')
   else:
       print('\033[0;31m''JOGO INVÁLIDO!')

elif computador ==2:
    if jogador==0:
       print('JOGADOR VENCEU!')
    elif jogador ==1:
        print('COMPUTADOR VENCEU!')
    elif jogador ==2:
        print('EMPATE!')
    else:
        print('\033[0;31m''JOGO INVÁLIDO!')

# Está com bug, não está lendo o else. (jogo inválido).

