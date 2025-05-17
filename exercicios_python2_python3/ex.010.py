from datetime import date
nasc=int(input('Ano de nascimento: '))
atual= date.today().year
idade= atual - nasc
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Categoria: MIRIM!')
elif idade <= 14:
    print('Categoria: INFANTIL!')
elif idade <=19:
    print('Categoria: JUNIOR!')
elif idade <= 20:
    print('Categoria: SÉNIOR!')
else:
    print('Categoria: MASTER!')

#from datetime import date: Esta instrução importa a classe date do módulo datetime. Isso significa que, após importar, você pode usar date para cria

# Módulo datetime: É uma biblioteca padrão do Python que fornece classes para  trabalhar com datas e horários. 

#Classe date: Um tipo de dado que representa uma data específica (ano, mês, dia). 

