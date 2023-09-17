# crie um programa que leia vários números inteiro pelo teclado. o programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. no final mostre quantos números foram digitados e quual foi a soma entre eles
n = soma = quant = 0
while True:
    n = int(input('digite um valor (999 para parar): '))
    if n == 999:
        break
    soma += n
    quant += 1
print(f'a soma dos {quant} valores foi {soma}')


