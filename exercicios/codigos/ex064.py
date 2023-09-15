# crie um programa que leia varios numeros inteiros pelo teclado, o programa só vai parar quando o usuário digitar 999 que é a condição de parada, no final, mostre quantos numeros foram digitados e qual foi a soma entre eles (Desconsiderando o Flag)
num = cont = soma = 0
num = int(input('digite um valor[999 parar]: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('digite um numero[999 parar]: '))
print(f'você digitou {cont} numeros e a soma entre eles foi {soma}')