# crie um programa que leia vários números inteiross pelos teclados, no final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos, o programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores
resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('digite um valor: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('quer continuar[S/N]: ')).strip().upper()
    media = soma / quant
print(f'você digitou {quant} valores e a média foi {media}')
print(f'o maior valor digitado foi {maior} e o menor {menor}')
