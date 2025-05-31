from random import choice
n1 = str(input('Digite nomes para o sorteio, 1º nome: '))
n2 = str(input('2º nome: '))
n3 = str(input('3º nome: '))
n4 = str(input('4º nome: '))

lista = [ n1, n2, n3, n4 ]
escl  = choice(lista)
print('Aluno escolhido para apagar o quadro: {}'.format(escl))

# "import choice" significa que estamos a importar a função que nos permite fazer uma escolha aleatória de um conjunto de itens. 

