from ex109 import moeda

p = float(input('Digite um preço: R$ '))
p = float(input('Digite um preço: R$ '))
print(f'A metade de {moeda.moeda(p, "€")} é {moeda.metade(p, True)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'O Aumento de 10% é {moeda.aumentar(p, True)}')
print(f'Ao diminur o valor em 10% {moeda.diminuir(p, True)}')
