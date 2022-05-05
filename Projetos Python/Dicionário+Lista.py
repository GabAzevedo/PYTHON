cadastro = list()
pessoa = dict()
soma = média = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome:'))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F]')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F ')
    pessoa['idade'] = int(input('Idade:'))
    soma += pessoa['idade']
    cadastro.append(pessoa.copy())
    resp = str(input('Quer continuar ? [S/N]')).upper()[0]
    while resp not in 'SN':
        print('ERRO!, responda apenas S ou N.')
        resp = str(input('Quer continuar ? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print('='*30)
print(f'A) Ao todo temos {len(cadastro)} pessoas cadastradas')
média = soma/len(cadastro)
print(f'B) A média de idade é de {média:5.2f} anos')
print('C) As mulheres cadastradas foram', end=' ')
for p in cadastro:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print()
print('D) Lista de pessoas que estão acima da média:')
for p in cadastro:
    if p["idade"] >= média:
        print('    ')
        for k,v in p.items():
            print(f'{k} = {v}; ', end=' ')
        print()
print('<< ENCERRADO >>')
