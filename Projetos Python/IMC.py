P = float(input('Qual é seu peso? (KG)'))
A = float(input('Qual é sua altura? (M)'))
imc = P/ (A ** 2)
print('O IMC dessa pessoa é de {:.2f}'.format(imc))
if imc <= 18.5:
    print('Você está ABAIXO DO PESO normal.')
elif imc <= 25:
    print('Você está no PESO IDEAL.')
elif imc <= 30:
    print('Você está SOBREPESO.')
elif imc <= 40:
    print('Você está em níveis de OBESIDADE.')
else:
    print('Você está em níveis de OBESIDADE MÓRBIDA.')