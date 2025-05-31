def ficha(nome='<desconhecido>', gol=0):
    print(f'{nome} fez {gol} no campeonato ')


n = str(input('Nome: '))
g = str(input('Gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)
