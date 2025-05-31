ficha = list()
cont = 0
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota1: '))
    nota2 = float(input('Nota2: '))
    média = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], média])
    r = str(input('Quer continuar ? [S/N] '))
    if r not in 'Ss':
        break
print('-=' * 15)
print(f'{"N.":<5}{"NOME":<10}{"MÉDIA":>8}')
print('-=' * 15)
for i, a in enumerate(ficha):
    print(f'{i:<5}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('---' * 20)
    resp = int(input('N° do aluno(a) p/ obter notas: [999 STOP] '))
    print('---' * 20)
    if resp == 999:
        break
    if resp <= len(
            ficha) - 1:  # opção para indentificar alunos, -1 é para contar o valor certo. menos 1 casa.
        print(f'Notas do aluno(a) {ficha[resp][0]}: {ficha[resp][1]}')
print('<<<<<<< FIM DO BOLETIM ESCOLAR! >>>>>>>>')
