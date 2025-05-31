time = list()
jogador = dict()
partidas = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    resp = (int(input(f'Quantas partidas {jogador["nome"]} jogou? ')))
    partidas.clear()
    for c in range(0, resp):
        partidas.append(int(input(f'  Quantos gols na partida {c + 1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        r = str(input('Quer continuar ? [S/N] ')).upper()[0]
        if r in 'SN':
            break
        print('Erro! digite novamente')
    if r == 'N':
        break
print('_' * 40)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('_' * 40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('_' * 40)
while True:
    busca = int(input('Mostrar os dado de qual jogador? (999 STOP) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Erro! Não existe jogador com o cod {busca}!')
    else:
        print(f'--- Levantamento do JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'   No jogo {i + 1} fez {g} gols.')
    print('-' * 40)
print('<< VOLTE SEMPRE >>> ')
