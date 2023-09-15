# crie um programa que leia o  ano de nascimento de 7 pessoas, no final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores
from datetime import date

maioridade = 0
menoridade = 0
atual = date.today().year

for pessoa in range(1, 8):
    
    nasc = int(input(f'em que ano a {pessoa}°pessoa nasceu?: '))
    idade = atual - nasc
    print(idade)

    if idade >= 21:
        maioridade += 1
    else:
        menoridade += 1

print(f'ao todo tivemos {maioridade} pessoas maiores de idade')
print(f'e também temos {menoridade} pessoas que é menor de idade') 
