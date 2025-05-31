lista = []
maior = 0
menor = 0
for c in range(0, 6):
    lista.append(int(input(f'Digite um valor na posição {c}: ')))
    if c == 0:
        maior = menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]
print('-=' * 23)
print(f'Você digitou os valores {lista}')
print(f'O maior valor digitado foi {maior} nas posições', end=' ')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i}... ', end=' ')
print()
print(f'O menor valor digitado foi {menor} nas posições', end=' ')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i}...', end=' ')
print()
print('-=' * 23)
print('Fim do programa!')


   
     #tipo: lista simples mutável 

     #lista.append(50)     # Adiciona um novo valor no final

     #enumerate(sequencia):

     #A função enumerate recebe uma sequência (como uma lista, tupla ou string) e #retorna um objeto iterável que produz pares de índice e valor.

     #i:
     #Em cada iteração, a variável i será atribuída a um par (índice, valor)

     #append() é um método usado para adicionar um novo elemento ao final de uma #lista
     
   
