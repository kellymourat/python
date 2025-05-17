dados = []
pessoas = []
maior = menor = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    res = str(input('Quer continuar ? '))
    if res not in 'Ss':
        break
print('»' * 40)
print(f'Total de {len(pessoas)} pessoas cadastradas!')
print(f'O maior peso foi {maior}kg. Peso de', end=' ')
for p in pessoas:
    if p[1] == maior:
        print(f'{p[0]}', end=' ')
print()
print(f'O menor peso foi de {menor} kg. Peso de ', end=' ')
for p in pessoas:
    if p[1] == menor:
        print(f'{p[0]}', end=' ')
print()
