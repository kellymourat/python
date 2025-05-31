import math
a=float(input('Comprimento do cateto oposto: '))
b=float(input('Comprimento do cateto adjacente: '))

c=math.hypot(a,b)
print('Hipotenusa = {:.2f}'.format(c))

# import math.hypot importa a função hypot() do módulo math. A função hypot() calcula a hipotenusa de um triângulo retângulo ou, mais genericamente, a norma euclidiana de um vetor. 