# Escreve um programa para aprovar o empréstimo bancário para a compra de uma casa. 

#o programa vai perguntar:
# valor da casa, 
# o salário do comprador 
# e em quantos anos ele vai pagar

# calcule o valor da prestação mensal. sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado

casa = float(input('digite o valor da casa: '))
salario = float(input('digite seu salário: '))
anos = int(input('quantos anos de financiamento: '))
prestacao = casa / (anos * 12)
minimo = salario * 30/100
print(f'pagar pagar uma casa de R${casa:.2f} em {anos} anos, a prestação será de {prestacao:.2f}')
if prestacao <= minimo:
    print('o emprestimo pode ser concebido')
else:
    print('o emprestimo não será concebido')
