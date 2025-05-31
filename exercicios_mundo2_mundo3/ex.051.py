print('»«'*20)
print('{:^40}'.format('TERMOS DE UMA PA'))
print('»«'*20)

primeiro=int(input('Primeiro termo: '))
razão=int(input('Segundo Termo: '))
décimo= primeiro + (10 -1) * razão
for c in range (primeiro, décimo + razão, razão):
    print('{}'.format(c),end=' -> ')



print('Acabou')


#"Progressão Aritmética" (PA) refere-se a uma sequência numérica onde a diferença entre termos consecutivos é constante. Essa constante é chamada de razão da PA. Em programação, pode-se usar Python para criar e trabalhar com PA, seja para gerar a sequência, calcular termos específicos, ou testar se uma sequência é uma PA.

#EXEMPLO:
#Uma Progressão Aritmética (PA) é uma sequência numérica onde cada termo é obtido somando-se um valor constante ao termo anterior. Por exemplo, a sequência 2, 4, 6, 8, ... é uma PA, com razão 2.
