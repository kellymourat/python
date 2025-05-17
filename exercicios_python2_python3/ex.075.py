n = (
     (int(input('digite número: '))),
     (int(input('Digite número: '))),
     (int(input('digite número: '))),
     (int(input('digite número: ')))
    )
print(f'Número 9 foi encontrado {n.count(9)} vezes.')
if 3 in n:
    print(f'Número 3 foi encontrado na {n.index(3) + 1}ª posição.')
else:
    print('Número 3 não foi encontrado!')
print(f'Números PARES digitados ', end='')
for c in n:
    if c % 2 == 0:
        print(c, end=' ')


    
    #tupla é uma sequência imutável de valores, geralmente usados para representar #registros ou coleções de dados que não devem ser alterados

    #Uma tupla em Python é imutável, ou seja:

    #Você pode ler os valores (acessar por índice, contar, buscar etc.).

    #Mas não pode alterar os valores depois que a tupla foi criada.

    #.index(3) significa que você está chamando o método .index() de uma lista, e o #argumento 3 é o valor que você quer encontrar na lista. O método .index() #retorna o índice (posição) do primeiro item na lista que é igual ao valor #especificado (no caso, 3). Se o valor não for encontrado, o método lança um #erro ValueError.
    
