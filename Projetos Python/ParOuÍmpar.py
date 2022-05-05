from random import randint
v = 0
print('='*30)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('='*30)

while True:
    jogador = int(input('Digite um valor:'))
    computador = randint(0,11)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I]')).strip().upper()[0]
    print('=' * 30)
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}')
    print('=' * 30)
    if tipo == 'P':
        if total % 2 == 0:
            print('VOCÊ VENCEU!')
            v += 1
        else:
            print('VOCÊ PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('VOCÊ VENCEU!')
            v += 1
        else:
            print('VOCÊ PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes.')
