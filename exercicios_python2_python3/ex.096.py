def lin():
    print('_' * 25)


def área(larg, comp):
    a = larg * comp
    print(f'A área do terreno {larg}x{comp} é de {a}m ')


print('  Controle de terreno  ')
lin()
l = int(input('Largura (m): '))
c = float(input('Comprimento (m): '))
área(l, c)
