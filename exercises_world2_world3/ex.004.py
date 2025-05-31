cont = soma = média = 0
n= 'S'
while n == 'S':
    num = int(input('Digite um número: '))
    n = str(input('Deseja continuar ? [S/N]: ')).upper().strip()[0]
    cont+=1
    soma+= num
    média= soma / cont
    if cont ==1:
        maior = num
        menor = maior
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor= num
print('Você digitou {} números, média entre eles {}.'.format(cont,média))
print('Maior n° lido {} menor n° {}.'.format(maior, menor))


