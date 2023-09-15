def Game_PedraPapelTesoura():
    # importando uma função que o computador jogue sozinho
    from random import randint
    from time import sleep
    itens = ('pedra', 'papel', 'tesoura')
    computador = randint(0,2)
    print('''suas opções:
    [ 0 ]pedra
    [ 1 ]papel
    [ 2 ]tesoura''')
    jogador = int(input('sua opção de jogada: '))
    print('jo')
    sleep(0.5)
    print('ken')
    sleep(0.5)
    print('po')
    sleep(0.5)
    print(f'o computador jogou {itens[computador]}')
    print(f'você jogou {itens[jogador]}')

    if computador == 0: #pedra
        if jogador == 0:
            print('empate')
        elif jogador == 1: #papel
            print('você venceu')
        elif jogador == 2:
            print('Computador venceu') #tesoura

    if computador == 1: #papel
        if jogador == 1:
            print('empate')
        elif jogador == 2: #tesoura
            print('você venceu')
        elif jogador == 0: #pedra
            print('computador venceu')
    
    if computador == 2: #tesoura
        if jogador == 2:
            print('empate')
        elif jogador == 0:
            print('você venceu')
        elif jogador == 1:
            print('computador venceu')


while True:
    resp = str(input('Outra jogada? [S/N]: ')).strip().upper()
    if resp in 'Ss':
        Game_PedraPapelTesoura()
    else:
        break