from datetime import date
atual= date.today().year
nasc=int(input('\033[0:32m''Ano de nascimento: ''\033[0:32m' '\033[m'))
idade= atual - nasc
print('Quem Nasceu no ano {} tem {} anos em {}.'.format(nasc,idade,atual))
if idade == 18:
    print('Você precisa se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo= 18 - idade
    print('Ainda Faltam {} anos para o alistamento militar'.format(saldo))
    ano= atual + saldo
    print (' Seu alistamento será em {}'.format(ano))
elif idade > 18:
    saldo= idade - 18
    print('Você ja deveria ter se alistado há {} anos.'.format(saldo))
    ano= atual - saldo
    print('Seu alistamento foi em {}.'.format(ano))








