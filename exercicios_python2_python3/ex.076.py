lista = ('Café', 2.50,
         'Açucar', 1.80,
         'Arroz', 0.98,
         'Feijão', 0.75,
         'Macarrão', 1.75,
         'Bolacha', 0.99,
         'Sabonete', 0.55,
         'Sabão', 4.52,
         'Uva', 1.99,
         'Banana', 1.99,
         'Pão', 1.75,
         'Água', 1.98,
         'Escova', 15.00,)
print('=' * 40)
print('{:^40}'.format(' LISTA DE PREÇOS '))
print('=' * 40)
for pos in range(len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<32}R$ ', end='')
    else:
        print(f'{lista[pos]:^5.2f}')
print('=' * 40)

   
    # Tupla 
    #[pos]: Indica que você está acessando um elemento específico da lista, com base #no índice pos.


   

 

