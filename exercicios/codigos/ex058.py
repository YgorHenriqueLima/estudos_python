# melhore o jogo de desafio 28 onde o computador vai pensar em um numero entre 0 e 10, só que agora o jogador vai tentar adivinhar até acertar, quantos palpites foram necessários para vencer
from random import randint
computador = randint(0, 30)
print('-='*30)
print('sou o computador... acabei de pensar em um numero entre 0 a 30, tente adivinhar')
print('-='*30)
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('qual seu palpite: '))
    palpites += 1
    if jogador < computador:
        print('mais... tente outra vez')
    elif jogador > computador:
        print('menos... ten10te outra vez')
    else:
        acertou = True
print(f'acertou com {palpites} tentativas, parabéns')