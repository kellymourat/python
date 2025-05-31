pessoas = dict()
galera = list()
soma = média = 0
while True:
    pessoas['nome'] = str(input('Nome: '))
    while True:
        pessoas['Sexo'] = str(input('Sexo: [F/M] ')).upper()[0]
        if pessoas['Sexo'] in 'FM':
            break
        print('Opção inválida digite F ou M.')
    pessoas['Idade'] = int(input('idade: '))
    soma += pessoas['Idade']
    galera.append(pessoas.copy())
    while True:
        resp = str(input('Quer continuar ? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('opção inválida digite S OU N.')
    if resp == 'N':
        break
print('_=' * 15)
print(f'A) Total de {len(galera)} pessoas cadastradas. ')
média = soma / len(galera)
print(f'B) Média da idade de pessoas cadrastradas {média:5.2f} anos.')
print('C) mulheres cadastradas foram: ', end='')
for p in galera:
    if p['Sexo'] in 'Ff':
        print(f' {p["nome"]}', end='')
print()
print('D) Lista de pessoas acima da média: ')
for p in galera:
    if p['Idade'] >= média:
        print('   ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<<<<<<<Encerrado>>>>>>')
