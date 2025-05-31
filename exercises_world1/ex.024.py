from random import shuffle
n1 = str(input('Digite nomes... 1º nome: '))
n2 = str(input('2º nome : '))
n3 = str(input('3º nome: '))
n4 = str(input('4º nome: '))

lista=[ n1, n2, n3, n4 ]
shuffle(lista)
print('Ordem de apresentação:')
print(lista)

# import random importa o módulo random, que fornece funções para gerar números pseudoaleatórios e outras operações relacionadas. A função shuffle dentro desse módulo é usada para embaralhar (misturar, desorganizar) os elementos de uma lista de forma aleatória, modificando-a diretamente.