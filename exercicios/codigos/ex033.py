a, b, c = int(input('primeiro valor: ')), int(input('segundo valor: ')), int(input('terceiro valor: '))

menor = a
if b < a and b < c:
    menor = b
elif c < a and c < b:
    menor = c

maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c


print(f'o menor valor digitado foi {menor} e o maior foi {maior}')