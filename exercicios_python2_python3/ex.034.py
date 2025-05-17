a = int(input('Primeiro número: '))
b = int(input('Segundo número: '))
c = int(input('Terceiro número: '))
# verificando quem é o menor valor
menor =  a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# verificando quem é o maior valor
maior= a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('Número menor é {}'.format(menor))
print('Número maior é {}'.format(maior))


