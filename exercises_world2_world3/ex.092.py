from datetime import datetime  # minha resolução

lista = dict()
cont = 0
while True:
    lista['Nome'] = str(input('Nome: '))
    nasc = int(input('Ano de nascimento: '))
    lista['Idade'] = datetime.now().year - nasc
    lista['CTPS'] = str(input('Carteira de trabalho? (0 não tem): '))
    cont += 1
    if lista['CTPS'] == 0:
        break
    elif lista['CTPS'] != 0:
        lista['Contratação'] = int(input('Ano de Contratação: '))
        lista['Salário'] = float(input('Sálario: '))
        lista['Aposentadoria'] = lista['Idade'] + ((lista['Contratação'] + 35) - datetime.now().year)
    break
print('-=' * 30)
for k, v in lista.items():
    print(f' -{k} tem o valor de {v}')
print(lista)

from datetime import datetime  # resolução professor!

lista = dict()
lista['Nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
lista['Idade'] = datetime.now().year - nasc
lista['CTPS'] = str(input('Carteira de trabalho? (0 não tem): '))
if lista['CTPS'] != 0:
    lista['Contratação'] = int(input('Ano de Contratação: '))
    lista['Salário'] = float(input('Sálario: '))
    lista['Aposentadoria'] = lista['Idade'] + ((lista['Contratação'] + 35) - datetime.now().year)
print('-=' * 30)
for k, v in lista.items():
    print(f' -{k} tem o valor de {v}')
print(lista)
