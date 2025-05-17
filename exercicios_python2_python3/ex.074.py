from random import randint

num = (randint(1, 10)), (randint(1, 10)), (randint(1, 10)), (randint(1, 10)), (randint(1, 10))
for c in num:
    print(f'{c}', end=' ')
print(f'\nO maior número sorteado: {max(num)}')
print(f'O menor número sorteado: {min(num)}')

# Tupla, não mutavél