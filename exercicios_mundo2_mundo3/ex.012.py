nome= str(input('Digite um nome ? ')).strip()
if nome == 'Berg':
     print('Que nome bonito você tem!')
elif nome == 'Catia' or nome== 'Pérola' or nome ==  'Preta' or nome== 'Maria':
     print('Esse nome é incrível e LINDO!')
elif nome in 'Antonia Cassia Luiz Henrique Jesus':
     print('Seu nome é de ANJO!')
else:
  print('Seu nome é bem comum! {}!'.format(nome))

print('Tenha um bom dia, {}!'.format(nome))

# uma estrutura aninhada significa que uma estrutura de controle, como if, for, while, ou um bloco de código, está contida dentro de outra estrutura do mesmo tipo ou de um tipo diferente. Isso permite a criação de lógica complexa, onde a execução de um bloco de código depende de condições ou iterações que, por sua vez, também dependem de outras condições ou iterações. 

# Tipos de estruturas:
# Simples, Composta e por fim, aninhada.

# uma estrutura aninhada if-elif-else permite verificar várias condições sequencialmente. O if inicia a verificação, e o elif (abreviação de else if) permite adicionar condições adicionais. O bloco de código associado à primeira condição verdadeira é executado, e as restantes são ignoradas, diz o DataCamp. 

#Significado:
#if:
#Verifica uma condição. Se for verdadeira, o bloco de código associado ao if é 

#executado.

#elif:
#(abreviação de else if) Verifica uma condição após uma ou mais condições if ou elif #anteriores terem sido falsas. Se a condição elif for verdadeira, o bloco de código #associado é executado.

#else:
#É uma cláusula final. Se todas as condições if e elif anteriores forem falsas, o #bloco de código associado ao else é executado.

# A estrutura if-elif-else é executada de cima para baixo. Se uma condição if for verdadeira, o seu bloco de código é executado, e as restantes condições ( elif e else) são ignoradas. Se a condição if for falsa, a verificação é continuada com a próxima condição elif. Se alguma elif for verdadeira, o seu bloco de código é executado, e as restantes são ignoradas. Se todas forem falsas, o bloco de código associado ao else é executado,
