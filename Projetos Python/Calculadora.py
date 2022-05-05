n1 = int(input('Primeiro valor:'))
n2 = int(input('Segundo valor:'))
opção = 0
while opção != 5:
    print('''    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa''')
    opção = int(input('Qual é sua opção?'))
    if opção == 1:
        soma = n1 + n2
        print('A soma dos valores {} + {} é igual a {}'.format(n1,n2, soma))
    elif opção == 2:
        produto = n1 * n2
        print('A multiplicação dos valores {} * {} é igual {}'.format(n1,n2,produto))
    elif opção ==3:
        if n1 > n2:
            maior = n1
            print('Entre {} e {} o maior valor é {}'.format(n1, n2, maior))
        else:
            maior = n2
    elif opção == 4:
        print('Informe os valores novamente:')
        n1 = int(input('Primeiro número:'))
        n2 = int (input('Segundo número:'))
    elif opção == 5:
        print('Finalizando...')
    else:
      print('Opção inválida, Tente novamente')
print('Fim do programa, volte sempre!')