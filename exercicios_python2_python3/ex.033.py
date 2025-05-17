from datetime import date
ano= int(input('Digite um ano, ou coloque (0) para analisar o ano atual. '))
if ano == 0:
    ano = date.today().year
if  ano % 4 == 0 and ano % 100 != 0 or ano % 400 ==0:
    print('Ano {} é BISSEXTO!'.format(ano))
else:
    print('Ano {} Não é BISSEXTO!'.format(ano))