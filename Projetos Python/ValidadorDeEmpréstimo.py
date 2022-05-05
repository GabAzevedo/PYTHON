C = int(input('Valor da casa: R$'))
S = float(input('Seu salário atual: R$'))
A = int(input('Em quantos anos pretende financiar?'))
P1 = C/A
P2 = P1/12
P3 = (S*30)/100
print('Para pegar uma casa de R$ {} em {} anos a prestação será de R$ {:.2F}'.format(C, A, P2))
if P2>P3:
    print('DEVIDO AO VALOR EXCEDER 30% DE SUA RENDA, SEU EMPRÉSTIMO FOI NEGADO!')
else:
    print('EMPRÉSTIMO PODE SER CONCEDIDO!')