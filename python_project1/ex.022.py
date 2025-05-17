from math import sin,cos,tan,radians
ang = float (input('Digite valor do ângulo:'))
seno = sin(radians(ang))
print('ângulo {} seu seno {:.2f}'.format(ang,seno))
cosseno = cos(radians(ang))
print('ângulo {} seu cosseno {:.2f}'.format(ang,cosseno))
tangente = tan(radians(ang))
print('ângulo {} seu tangente {:.2f}'.format(ang,tangente))


# import math importa o módulo math, que contém funções matemáticas, incluindo funções trigonométricas como sin, cos e tan. Estas funções calculam o seno, cosseno e tangente, respetivamente, de um ângulo fornecido em radianos. math.radians() é utilizada para converter ângulos de graus para radianos, pois as funções sin, cos e tan do módulo math esperam a entrada em radianos.



