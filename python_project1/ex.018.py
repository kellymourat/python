from math import trunc
num= float(input('Digite um número:'))
print('Número digitado {} sua porçao inteira {}.'.format(num,trunc(num)))

num = float(input('Digite um número:'))
print('Número digitado {} sua porçao inteira {}.'.format(num,int(num)))

#  math.trunc() é uma função que retorna a parte inteira de um número, removendo a parte decimal (fracionária). Ou seja, ela simplesmente desconsidera as casas decimais, sem arredondar para cima ou para baixo. 