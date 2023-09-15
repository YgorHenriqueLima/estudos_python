# desenvolva um programa que leia seis numeros inteiros e mostre a soma apenas daqueles que forem par, se o valor digitador for impar, desconsidere-o
soma = 0
cont = 0
for c in range(1, 7):
    num = int(input(f'digite o {c}°valor: '))
    if num % 2 == 0:
        soma += num
        cont += 1
print(f'você imformou {cont} numeros e a soma entre eles foi {soma}')    
