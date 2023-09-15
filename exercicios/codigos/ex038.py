def linha():
    print('-'*30)

def comando():
    linha()
    n1 = int(input('digite um valor: '))
    n2 = int(input('digite outro valor: '))
    linha()
    if n1 > n2:
        print(f'\033[34m{n1} é maior que {n2}\033[34m')
    elif n1 < n2:
        print(f'\033[31m{n1} é menor que {n2}\033[31m')
    elif n1 == n2:
        print(f'{n1} é igual a {n2}')


resp = str(input('rode o programa [S/N]')).strip().upper()
while resp not in 'Nn':
    comando()
    resp = str(input('quer continuar [S/N]')).strip().upper()
    if resp == 'S':
        comando()
    else:
        print('fim do programa')
        break