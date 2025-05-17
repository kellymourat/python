'''aluno= dict()
aluno['nome']=str(input('Nome: '))
aluno['média']=float(input(f'A média da {aluno["nome"]}: '))
if aluno['média'] >=7:
    aluno['Situação'] = 'APROVADO!'
elif 5 <= aluno['média'] <7:
    aluno['Situação'] = 'RECUPERAÇÃO!'
else:
    aluno['Situação'] = 'REPROVADO!'
for k, v in aluno.items():
    print(f'{k} é igual a {v}')'''

aluno = {'nome': str(input('Nome: ')), 'nota': float(input('Nota: '))}  # minha resolução
print(f'Nome é igual a {aluno["nome"]}')
print(f'Média é igual a {aluno["nota"]}')
if aluno["nota"] >= 7:
    print(f'Situação é igual a APROVADO!')
else:
    print(f'Situação é igual a REPROVADO!')
