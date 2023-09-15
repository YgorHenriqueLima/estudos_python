# faça um programa que leia o peso de cinco pessoas, no final mostre qual foi o maior e o menor peso lidos
lista = []
for p in range(1, 6):
    lista.append(float(input(f'peso da {p}°pessoa: ')))
print(f'o maior peso lido foi de {max(lista)}kg')
print(f'o menor peso lido foi de {min(lista)}kg')