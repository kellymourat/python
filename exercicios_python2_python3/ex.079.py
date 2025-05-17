numeros = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado na lista...')
    else:
        print('valor duplicado, Não irei adicionar...')
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
numeros.sort()
print(f'Você digitou os valores {numeros}.')


   
    #Se você precisa ordenar uma lista sem criar uma cópia, use o método .sort().
    #Se você precisa manter a lista original e obter uma nova ordenada, use a função #sorted().



