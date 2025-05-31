print('{:=^40}'.format(' LOJAS KELLY '))
preço=int(input('Preço das compras ? R$ ' ))
print('''FORMA DE PAGAMENTO
[ 1 ] À vista dinheiro/cheque 
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção=int(input('Opções de pag ? '))
if opção == 1:
    total = preço - ( preço * 10 / 100)
elif opção == 2:
    total = preço - ( preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela= preço / 2
    print('Sua compra de R${:.2f} parcelado 2x no cartão fica R${:.2f} por mês, SEM JUROS!'.format(preço,parcela))
elif opção == 4:
     total= preço + ( preço * 20 / 100)
     totparc= int(input('Quantas parcelas ? '))
     parcela = total / totparc
     print('Sua compra será parcelada em {}x de  R${:.2f} COM 20% de JUROS!.'.format(totparc,parcela))
else:
    total = preço
    print('\033[0;31m' 'OPÇÃO INVÁLIDA de PAG. Tente novamente!''\033[m')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço,total))




