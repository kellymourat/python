from time import sleep


def lin():
    print('-=' * 20)


def maior(*num):
    cont = maior = 0
    print(f'Analizando os valores passados...')
    for valor in num:
        print(f'{valor}', end=' ')
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}')
    lin()


maior(2, 10, 4, 5, 1)
maior(4, 7, 0, 6)
maior(1, 2)
maior(6)
maior(0)
