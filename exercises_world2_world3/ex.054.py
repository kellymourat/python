from datetime import date
atual = date.today().year
cont=0
tot=0
for pess in range(1,8):
    nasc=int(input('Em que ano {}ª pessoa nasceu? '.format(pess)))
    idade= atual - nasc
    if idade >= 21:
        cont += 1
    else:
        tot += 1
print('Total de pessoas maiores de idade: {}'.format(cont))
print('Total de pessoas menores de idade: {}'.format(tot))

# data.today().year é uma expressão que retorna o ano da data atual.
    
#Explicação:

#datetime.date.today():
#Esta parte do código utiliza a função today() do módulo datetime para obter a data do dia atual.

#.year:
#Após obter a instância da data atual, o atributo .year extrai o ano específico da data.

    