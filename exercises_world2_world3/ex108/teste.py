from ex109 import moeda

p = float(input('Digite um preço: R$ '))
print(f'A metade de {moeda.moeda(p, "€")} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'O Aumento de 10% é {moeda.moeda(moeda.aumentar(p))}')
