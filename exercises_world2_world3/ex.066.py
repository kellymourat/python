cont = soma = 0
while True:
    num = int(input('Digite o número (999 STOP): '))
    if num == 999:
        break  # Interrompe o loop quando num é igual 999
    cont+=1
    soma+=num
print(f'Soma dos {cont} valores lidos foi {soma}!')

   #break é uma palavra-chave usada para interromper a execução de um loop (como for ou while) antes que ele termine naturalmente. Quando break é encontrado dentro de um loop, a execução do loop é imediatamente encerrada e o código volta a ser executado na primeira linha após o loop. 

   
  



