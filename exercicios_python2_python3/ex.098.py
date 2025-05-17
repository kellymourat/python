from time import sleep


def lin():
    print('-=' * 20)


def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    lin()
    print(f'Contagem de {i} até {f} de {p} em {p}!')
    sleep(0.2)

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=' ')
            sleep(0.2)
            cont += p
        print('Fim!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ')
            sleep(0.2)
            cont -= p
        print('Fim!')


contador(1, 10, 1)
contador(10, 0, 2)
lin()
print('Agora é sua vez de personalizar a sua contagem!')
ini = int(input('Inicio: '))
fim = int(input('fim:   '))
pas = int(input('Passo: '))
contador(ini, fim, pas)
