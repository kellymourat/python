cont = ('zero', 'um', 'dois', 'três', 'quatro',
        'cinco', 'seis', 'sete', 'oito', 'nove',
        'dez', 'onze', 'doze', 'treze', 'catorze',
        'quinze', 'dizesseis', 'dizessete',
        'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input('Digite um número entre 0 a 20: '))
    if 0 <= num <= 20:
        print(f'Você digitou o número {cont[num]}')
    else:
        print('Número inválido digite entre 0 e 20:')
    n = ' '
    while n not in 'SN':
        n = str(input('Quer continuar ? [S/N] ')).upper()
    if n != 'S':
        break
print('Fim!')
