preco = float(input('digite um preço R$: '))
novo = preco - (preco * 15/100)
print('o produto que custava {} na promoção com desconto de 15% de desconto passou a ganhar R${:.2f}'.format(preco, novo))