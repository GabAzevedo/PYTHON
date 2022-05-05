Time = list()
Jogador = dict()
partidas = list()

while True:
    Jogador.clear()
    Jogador['Nome'] = str(input('Nome do Jogador:'))
    tot = int(input(f'Quantas partidas {Jogador["Nome"]} jogou?'))
    partidas.clear()
    for c in range(0,tot):
        partidas.append(int(input(f'Quantos gols na partida {c+1}?')))
    Jogador['gols'] = partidas[:]
    Jogador['total'] = sum(partidas)
    Time.append(Jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]'))
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('='*30)
print('cod', end='')
for i in Jogador.keys():
    print(f'{i:<15}', end='')
print()
print('='*40)
for k, v in enumerate(Time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('='*40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(Time):
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {Time[busca]["nome"]}:')
        for i,g in enumerate(Time[busca]['gols']):
            print(f'  No jogo {i} fez {g} gols')
    print('='*40)
print('<< VOLTE SEMPRE >>')
