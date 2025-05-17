from random import randint
from time import sleep
from operator import itemgetter

print('«««« VALORES SORTEADOS »»»»»')
jogo = {'Jogador1': randint(1, 7),
        'Jogador2': randint(1, 7),
        'Jogador3': randint(1, 7),
        'Jogador4': randint(1, 7)}
ranking = list()
for k, v in jogo.items():
    print(f'{k} Tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('  == RANKING DO JOGO ==   ')
for i, v in enumerate(ranking):
    print(f'{i + 1}º lugar: {v[0]} com {v[1]}.')
print(ranking)
