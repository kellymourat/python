totH = totM = totP = 0
print('='*40)
print('{:^40}'.format(' CADASTRO DE PESSOAS '))
print('='*40)
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        totP += 1
    if sexo in 'mM':
        totH += 1
    if sexo in 'fF' and idade < 20:
        totM += 1
    c = ' '
    while c not in 'SN':
        c = str(input('Deseja continuar ? [S/N] ')).strip().upper()[0]
        print('=' * 40)
        print('{:^40}'.format(' CADASTRO DE PESSOAS '))
        print('=' * 40)
    if c != 'S':
        break
print(f'{totP} pessoas maiores de 18 anos.')
print(f'Total de {totH} homens.')
print(f'{totM} pessoas do sexo feminino menores de 20 anos.')

 
    #obs: se não colocar às três últimas linhas, o código não faz a contagem de da forma correta.
    #colocando uma variable com espaço vazio e um while loop faz repetir várias vezes até colocar a opção certa.

  
