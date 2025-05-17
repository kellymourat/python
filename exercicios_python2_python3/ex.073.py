time = ('gremio', 'palmeiras', 'santos', 'corinthians', 'atletico Mineiro',
        'cruzeiro', 'internacional', 'são paulo', 'flamengo',
        'fluminence', 'atletico Paranaense', 'botafogo', 'vasco da Gama',
        'coritiba', 'ponte preta', 'figueirense', 'sport', 'goias', 'chapecoense', 'vitoria')
print('»' * 50)
print(f'Os 5ª colocados: {time[0:5]}')
print('»' * 50)
print(f'Os 4ª ultímos são: {time[-4:]}')
print('»' * 50)
print(f'Time em ordem alfabética: {sorted(time)}')
print('»' * 50)
print(f'O chapecoense está na: {time.index("chapecoense")}ªposição')


# Tupla imutável