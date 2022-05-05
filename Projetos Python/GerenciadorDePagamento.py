preço = float(input('Preço das compras: R$'))
print('''FORMA DE PAGAMENTO'
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Qual é a forma de pagamento?'))
if opção == 1:
    print('Na opção de compra a vista em dinheiro/cheque, você tem direito a 10% de desconto')
    total = preço - (preço*10)/100
    print('Valor total da compra com desconto é R${:.2F}'.format(total))
elif opção == 2:
    print('Na opção de compra a vista no cartão, você tem direito a 5% de desconto')
    total = preço - (preço*5)/100
    print('O valor total da compra com desconto é R${:.2F}'.format(total))
elif opção == 3:
    print('Na opção de compra em 2x no cartão, o preço permanece o mesmo.')
    total=preço/2
    print('Sua compra parcelada em 2x sairá a R${:.2F} por parcela'.format(total))
elif opção == 4:
    print('Na opção de compra em 3x ou mais, estará sujeito a juros de 20%.')
    total = preço + (preço*20)/100
    totparc = int(input('Quantas parcelas?'))
    parcela = total / totparc
    print('Sua compra será parcelada em {}x de R$ {:.2F} COM JUROS'.format(totparc, parcela))
    print('Sua compra de R${:.2F}, vai custar R${:.2F} no final'.format(preço,total))