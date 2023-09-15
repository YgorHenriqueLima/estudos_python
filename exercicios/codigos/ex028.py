# escreva um progrma que faça o computador "pensar" num número inteiro aleatório
# entre 0 e 5 e peça para que o usuario tente descobrir qual foi o número escolhido pelo Pc

import random
from time import sleep

def anin():
    sleep(1)
    print('-=' * 30)


#numero aleatório entre 0 e 5
computador = random.randint(0, 5)
anin()
print('\033[31mpensei em um numero aleatório entre 0 e 5, tente adivinhar...\033[m')
anin()

# o número que o jogador vai digitar
jogador = int(input('qual numero eu pensei?: '))
print('processando')
sleep(1)

#condições
while True:
    if jogador == computador:
        print(f'você acertou, eu pensei também no numero {computador}')
        break
    else:
        print(f'você errou, não pensei no {jogador} pensei no {computador}')
        resp = str(input('quer continuar [S/N]')).strip().upper()
        if resp in 'Nn':
            break
        if resp in 'Ss':
            computador = random.randint(0, 5)
            anin()
            print('\033[31mpensei em um numero aleatório entre 0 e 5, tente adivinhar...\033[m')
            anin()

            # o número que o jogador vai digitar
            jogador = int(input('qual numero eu pensei?: '))
            print('processando')
            sleep(1)
            if jogador == computador:
                print(f'você acertou, eu pensei também no numero {computador}')
            else:
                print(f'você errou, não pensei no {jogador} pensei no {computador}')
