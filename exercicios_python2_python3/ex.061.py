print('»'*35)
print('{:^35}'.format('TERMOS DE UMA PA'))
print('»'*35)
p=int(input('Primeiro Termo: '))
r=int(input('Segundo Termo: '))
termo= p
cont=0
while cont < 10:
    print('{}'.format(termo),end= '->')
    termo += r
    cont+=1
print('Fim!')


    
     #Função: "While" cria um loop de repetição, executando um bloco de código repetidamente enquanto uma condição for verdadeira.
    