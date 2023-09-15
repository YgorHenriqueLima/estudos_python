# refaça o desafio 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while
print('gerador de pa')
print('-='*10)
a1 = int(input('primeiro termo: '))
r = int(input('razão: '))
print('-='*10)
termo = a1
cont = 1
while cont <= 10:
    print(f'{termo} ->', end=" ")
    termo += r
    cont += 1

