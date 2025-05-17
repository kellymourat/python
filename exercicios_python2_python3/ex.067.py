print('{:=^100}'.format('TABUADA'))
while True:
    print('_' * 35)
    tab=int(input('Digite o número da sua tabuada: '))
    print('_' * 35)
    if tab <=0:
        break
    for c in range(1,11):
     print(f'{tab} x {c} = {tab*c}')
print('Fim da TABUADA!')


  
     #while True cria um loop infinito. A instrução while executa o bloco de código dentro dela repetidamente enquanto a condição for verdadeira. True é uma expressão que sempre é verdadeira, então o loop continuará indefinidamente até ser interrompido por uma instrução de break dentro do loop. 

  