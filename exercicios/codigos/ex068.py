# programa par ou impar
# o jogo só será imterrompido quando o jogador PERDER, mostrando:
# -> o total de vitórias consecutivas que ele conquistou no final do jogo
from random import randint
vitoria = 0
while True:

    print('-='*30)
    jogador = int(input('digite um valor: '))
    computador = randint(1, 11)
    total = jogador + computador
    tipo = ''
    tipo = str(input('par ou impar [P/I]: ')).strip().upper()
    print('-='*30)

    print(f'jogador jogou {jogador} e computador {computador} e o total {total}')
    print(f'deu par' if total % 2 == 0 else 'deu impar')

    if tipo == 'P':
        if total % 2 == 0:
            print('você venceu')
            vitoria += 1
        else:
            print('você perdeu')
            break

    elif tipo == 'I':
        if total % 2 == 1:
            print('você venceu')
            vitoria += 1
        else:
            print('você perdeu')
            break