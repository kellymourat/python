from ex107.moeda import metade, dobro, aumentar, moedas

p = float(input('Digite um preço: R$ '))
print(f'A metade de R$ {p} é R$ {metade(moedas(p))}')
print(f'O dobro de R$ {p} é R$ {dobro(moedas(p))}')
print(f'Aumento 10% temos R$ {aumentar(moedas(p))}')
