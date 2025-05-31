from time import sleep

c = ('\033[m',  # 0 - sem cores
     '\033[0;41m',  # 1 - vermelho
     '\033[0;42m',  # 2 - verde
     '\033[0;43m',  # 3 - amarelo
     '\033[0;44m',  # 4 - azul
     '\033[0;45m',  # 5 - roxo
     '\033[0;46m',  # 6 - ceano
     '\033[0;47m',  # 7 - cinza
     '\033[7;40m',  # 8 - branco
     )


def ajuda(com):
    título(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[8], end='')
    help(com)
    print(c[0], end='')
    sleep(2)


def título(msg, cor=0):
    tan = len(msg) + 4
    print(c[cor], end='')
    print('~' * tan)
    print(f'  {msg}')
    print('~' * tan)
    print(c[0], end='')
    sleep(1)


# programa princípal
comando = ''
while True:
    título('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('função ou bíblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
título('ATÉ LOGO!', 1)
