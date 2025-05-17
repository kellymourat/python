somaid = 0
médiaid = 0
maioridh= 0
nold = ''
mulher20= 0
for p in range(1, 5):
    print('===== {}ª Pessoa ======'.format(p))
    nome=str(input('Nome: ')).strip().upper()
    idade=int(input('Idade: '))
    sexo=str(input('Sexo [M/F]: ')).strip().upper()
    somaid += idade
    médiaid = somaid / 4
    if p == 1 and sexo in 'Mm':
        maioridh = idade
        nold = nome
    if sexo in 'Mm' and idade > maioridh:
        maioridh = idade
        nold= nome
    if sexo in 'Ff' and idade <=20:
        mulher20 += 1
print('Média de idade do grupo é de {}'.format(médiaid))
print('Homem mais velho tem {} anos e seu nome {}'.format(maioridh,nold))
print('Total de mulheres com menos de 20 anos {}'.format(mulher20))

