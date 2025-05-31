nome=str(input('nome completo:')).strip()
print('Seu nome em maiúscula é {}'.format(nome.upper()))
print('Seu nome em minúscula é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras,sem espaços.'.format(len(nome)-nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))

#separa= nome.split()
#print('Seu primeiro nome é {} tem {} letras'.format(separa[0],len(separa[0])))

# upper() é um método de string que converte todos os caracteres de uma string para letras maiúsculas. Por exemplo, se você tiver a string "Olá, Mundo!", upper() converterá essa string para "OLÁ, MUNDO!".

# lower() é um método de string que converte todos os caracteres de uma string para letras minúsculas. Isso significa que qualquer letra maiúscula na string será transformada na sua versão minúscula correspondente. 

# len() é uma função embutida que retorna o número de itens de um objeto iterável, como uma string, lista, tupla ou dicionário. Por exemplo, len("Olá, mundo") retorna 10, pois a string "Olá, mundo" tem 10 caracteres.

#  "count" (contar) refere-se a um método usado para contar o número de vezes que um determinado valor ou elemento aparece numa lista, string ou outro tipo de sequência. É uma forma eficiente de verificar a frequência de ocorrências em um conjunto de dados.

#  "count" (contar) refere-se a um método usado para contar o número de vezes que um determinado valor ou elemento aparece numa lista, string ou outro tipo de sequência. É uma forma eficiente de verificar a frequência de ocorrências em um conjunto de dados. 