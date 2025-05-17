nome= str(input('digite o nome completo:')).strip()
print ('Muito prazer em te conhecer, {} !'.format(nome))
n= nome.split()
print('Seu primeiro nome; {}'.format(n[0]))
print('Seu último nome; {}'.format(n[len(n)-1]))

# split() é uma função que divide uma string em uma lista de substrings. Por padrão, a função usa espaços em branco como separador, mas você pode especificar outro separador (como vírgula, ponto, etc.). A função também permite limitar o número máximo de divisões. 
