num= int(input('Digite o número inteiro: '))
print('''Escolha uma das bases de conversão: 
[1] para BINÁRIO
[2] para OCTAL
[3] para HEXADECIMAL''')
opção= int(input('Sua opção:'))
if opção == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin (num)[2:]))
elif opção == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct (num)[2:]))
elif opção == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format( num, hex(num)[2:]))
else:
    print('Opção INVÁLIDA! Tente Novamente!')


#  bin(), oct() e hex() são funções embutidas que convertem um número decimal para sua representação binária, octal e hexadecimal, respetivamente. Elas são úteis para trabalhar com diferentes bases numéricas.

# bin(x):
# Converte o inteiro x para sua representação binária (base 2), retornando uma string # com o prefixo "0b".

# oct(x):
# Converte o inteiro x para sua representação octal (base 8), retornando uma string # com o prefixo "0o".

# hex(x):
# Converte o inteiro x para sua representação hexadecimal (base 16), retornando uma # string com o prefixo "0x".

# [2:] é uma forma de fatiamento de sequência, que permite extrair uma parte de uma sequência (como uma lista, string, tupla, etc.). Neste caso, [2:] significa:
#Começar do índice 2:

#O primeiro elemento da sequência tem o índice 0, o segundo tem o índice 1, e assim #por diante. [2:] indica que a extração deve começar a partir do terceiro elemento #da sequência.

#Até o final:
#O ponto "..." após o índice 2 indica que a extração deve continuar até o último #elemento da sequência.



