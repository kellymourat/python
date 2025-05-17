exp = str(input('Digite a sua expressão: '))
pilha = []
cont = cont1 = 0
for simb in exp:
    if simb == '(':
        pilha.append('(')
        cont += 1
    elif simb == ')':
        pilha.append(')')
        cont1 += 1
        if cont == cont1:
            print('Expressão VÁLIDA!')
        else:
            print('Expressão INVÁLIDA!')
        break
exp = str(input('Digite a sua expressão: ')) 
pilha = []
for simb in exp:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
        break
if len(pilha) == 0:
    print('Essa expressão é VÁLIDA!')
else:
    print('Expressão INVÁLIDA!')
print(pilha)
