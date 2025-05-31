soma = 0
for c in range (1, 7):
    num = int(input('Digite o {} número: '.format(c)))
    if num % 2 ==0:
      soma += num
    else:
        print('\033[0;31m''Valor IMPAR, tente novamente!''\033[m')
print('\033[0;33m''Soma total dos valores PARES {}.'.format(soma))

# Porfessor Guanabara 
soma = 0
cont= 0
for c in range (1,7):
    num=int(input('Digite o {} número: '.format(c)))
    if num % 2 ==0:
        soma += num
        cont +=1
print('Você informou {} números PARES e a soma total foi {}.'.format(cont,soma))

# cont += 1 significa que o valor da variável cont é incrementado em 1. Isso é uma forma abreviada de escrever cont = cont + 1. A instrução soma o valor atual da variável cont com 1 e atribui o resultado de volta à variável cont.