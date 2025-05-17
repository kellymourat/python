from math import sqrt, floor
num= int(input('Digite um número:'))
raiz= sqrt(num)
print ('raiz de {} = {:.2f}'.format(num, floor (raiz)))

# import math, math.sqrt() e math.floor() são funções que pertencem ao módulo math. import math importa o módulo, math.sqrt() calcula a raiz quadrada de um número, e math.floor() arredonda um número para baixo (para o inteiro mais próximo menor ou igual ao número).