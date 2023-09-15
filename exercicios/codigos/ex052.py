# faça um programa que leia um numero inteiro e diga se ele é ou não um numero primo
num = int(input('digite um numero: '))
tot = 0
for c in range(1, num+1):
    if num % c == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print(f'{c}', end='')
print(f'\033[m o numero {num} foi divisivel {tot} vezes')
if tot == 2:
    print(f'e por isso que ele é primo!')
else:
    print('e por isso ele não é primo')
