from random import randint
from time import sleep
computador = randint(0,5) # faz o computador "pensar"
print ('\033[0;30;43m''--==--''\033[m'*10)
print('\033[0;30;43m' 'Vou pensar em um número entre 0 e 5. Tente adivinhar...     ''\033[m')
print ('\033[0;30;43m''--==--''\033[m'*10 )
jogador=int(input('\033[0;30;41m''Em que número pensei ?''\033[m')) # Jogador tenta adivinhar
print ('\033[35m''Processando...\033[m')
sleep(1)
if jogador == computador:
    print('Parabéns, você conseguiu me vencer! :(  ')
else:
    print('Vixiii... caba sem sorte, você PERDEU! Pensei no número {}, você escolheu {} :( '.format(computador, jogador))

# randint é uma função do módulo random que gera um número inteiro aleatório dentro de um intervalo especificado. A função randint(a, b) retorna um número inteiro N tal que a <= N <= b, ou seja, os limites inferior (a) e superior (b) são inclusivos. 

# randint(a, b) gera um número inteiro entre a e b (inclusive).
# O módulo random deve ser importado para usar randint.
# A função é útil em diversas aplicações, como jogos, simulações e testes


