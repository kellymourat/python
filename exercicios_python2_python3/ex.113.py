def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO digite um número inteiro válido!\033[m')
            continue
        except KeyboardInterrupt:
            print('\n \033[0;31m Usuário preferiu não digitar esse número \033[m')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[0:31mERRO digite um valor válido!\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[0;31m Usuário optou em não digitar nada.\033[m')
            return 0
        else:
            return n


num = leiaInt('Digite um valor inteiro: ')
n = leiaFloat('Digite um valor real: ')
print(f'Valor em real {n}, valor inteiro {num}.')
