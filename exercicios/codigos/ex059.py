# crie um programa que leia dois valores e mostre um menu na tela de somar, multiplicar, maior, novos numeros, sair do programa, e seu programa deverá realizar a operação solicitada em cada caso
from time import sleep
n1 = int(input('primeiro valor: '))
n2 = int(input('segundo valor:  '))
sleep(0.5)
opcao = 0
while opcao != 5:
    print('''diga a opção:
        [ 1 ]somar
        [ 2 ]multiplicar
        [ 3 ]maior
        [ 4 ]novos valores
        [ 5 ]sair do programa''')
    opcao = int(input('digite sua opção: '))

    if opcao == 1:
        s = n1 + n2
        print(f'a soma entre {n1} + {n1} é {s}')

    elif opcao == 2:
        m = n1 * n2
        print(f'a multiplicação entre {n1} e {n2} é {m}')

    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'o maior valor valor entre {n1} e {n2} é {maior}')

    elif opcao == 4:
        print('informe os numeros')
        n1 = int(input('primeiro valor: '))
        n2 = int(input('segundo valor: '))
    
    elif opcao == 5:
        print('finalizando')
    else:
        print('opção inválida, tente novamente')
    print('-='*30)
    print('fim do programa')
