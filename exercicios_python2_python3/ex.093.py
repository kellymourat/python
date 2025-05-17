jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do jogador: '))
resp = (int(input(f'Quantas partidas {jogador["nome"]} jogou? ')))
for c in range(0, resp):
    partidas.append(int(input(f'  Quantos gols na partida {c}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('_=' * 30)
print(jogador)
print('_=' * 30)
for k, v in jogador.items():
    print(f' O campo {k} tem o valor {v}')
print('_=' * 30)
print(f' O jogador {jogador["nome"]} jogou {len(jogador)} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f' --> Na Partida {i}, fez {v} gols. ')
print(f' foi um total de {jogador['total']} gols.')
