from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo Valor: '))
opç= 0
while opç != 5:
      print('''Opções:
      [1] Somar
      [2] Multiplicar
      [3] Maior valor
      [4] Novos valores 
      [5] Sair do programa.''')
      opç=int(input(' >>>>> Digite sua opção: '))
      if opç ==1:
          soma= n1 + n2
          print( 'A soma {} + {} é = {}'.format(n1,n2,soma ))
      elif opç ==2:
          mult= n1 * n2
          print('A multiplicação de {} x {} = {}'.format(n1,n2,mult))

      elif opç ==3:
          if n1 > n2:
              maior= n1
          else:
              maior= n2
          print('O maior número entre {} e {} = {}'.format(n1,n2,maior))

      elif opç == 4:
          print('digite Novos valores!')
          n1=int(input('Primeiro número:'))
          n2=int(input('Segundo número: '))

      elif opç ==5:
          print('Finalizando os calculos!')

      else:
          print('Opção inválidada! Digite opções disponíveis.')
      print('»»»»»'*10)
      sleep(2)
print('Obrigado Volte sempre!')




