# leia o nome e o preço de (vários produtos)
# o programa deverá perguntar se o usuário vai continuar no final, mostre 

#A) qual é o total gasto na compra
#b) quantos produtos custam mais de R$1000
#c) qual é o nome do produto mais barato 
print('-='*30)
print('loja barata')
print('-='*30)
total = totmil = menor = cont = 0

while True:
    produto = str(input('nome do produto: '))
    preco = float(input('Preço: R$'))

    cont += 1
    total += preco
  
    if preco > 1000:
        totmil += 1
  
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto

    resp = ' '
    while resp not in 'SN':
        resp = str(input('quer continuar[S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break

print(f'o total gasto na compra foi {total:.2f}')
print(f'temos {totmil} produtos acima de R$1000')
print(f'o preço mais barato da compra foi {menor}')