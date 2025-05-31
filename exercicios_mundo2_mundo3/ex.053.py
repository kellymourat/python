frase = str(input('Digite uma frase: ')).strip().upper()
palavra= frase.split()
junto=''.join(palavra)
inverso = junto[::-1]
print('O inverso de {}, é {}.'.format(junto,inverso))
if inverso == junto:
       print('Temos um PALÍNDROMO!')
else:
      print('A frase não é um PALÍNDROMO!')


'''frase = str(input('Digite uma frase: ')).strip().upper()
palavra= frase.split()
junto=''.join(palavra)
inverso = ''
for letra in range (len(junto)-1,-1,-1):
    inverso += junto [letra]
print('O inverso de {}, é {}.'.format(junto,inverso))
if inverso == junto:
       print('Temos um PALÍNDROMO!')
else:
      print('A frase não é um PALÍNDROMO!')'''

#Progama tem duas formas de ser executado!

#Primeiro com for
#Segundo com fatiamento no python.

#palíndromo é uma sequência de caracteres (string) que se lê da mesma forma de frente para trás e de trás para frente. Por exemplo, "radar", "madam" e "arara" são palíndromos

#.split() é um método de string que divide uma string em uma lista de substrings, usando um separador especificado como argumento.
    
     '''  sem separdor:

       frase = "Olá, mundo!"
       lista_de_palavras = frase.split()
       print(lista_de_palavras)  # Saída: ['Olá,', 'mundo!']

       com separador específico:

       frase = "1,2,3,4,5"
       lista_de_números = frase.split(",")
       print(lista_de_números)  # Saída: ['1', '2', '3', '4', '5']

       Com separador e número máximo de divisões:

       frase = "a,b,c,d,e"
       lista_de_substrings = frase.split(",", 2)
       print(lista_de_substrings)  # Saída: ['a', 'b', 'c,d,e']'''



       


#texto[::-1]: Cria uma cópia invertida da string usando o slicing [::-1].

# .join() é um método usado para concatenar (juntar) os elementos de um iterável (como uma lista, tupla ou string) em uma única string. Ele insere uma string especificada como separador entre cada elemento do iterável. 
     '''
       palavras = ["Olá", "mundo", "!" ]
       separador = " "
       frase = separador.join(palavras)
       print(frase) # Saída: Olá mundo !
     '''




