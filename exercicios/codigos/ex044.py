# elabora um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - a vista dinheiro/cheque: -> 10% de desconto
# - a vista cartão: 5% de desconto

def programa_preco():
        print('{:=^40}'.format('LOJAS TECNOLOGIAS'))
        preco = float(input('preço da compra: R$'))
        print('''formas de pagamento:
        [ 1 ] à vista dinheiro/cheque
        [ 2 ] à vista cartão
        [ 3 ] 2x no cartão
        [ 4 ] 3x ou mais no cartão
        ''')
        opcao = int(input('qual é a sua opção?: '))
        if opcao == 1:
            total = preco - (preco * 10/100)
            print(f'sua compra de R${preco:.2f} vai custar R${total:.2f} no final')

            
        elif opcao == 2:
            total = preco - (preco * 5/100)
            print(f'sua compra de R${preco:.2f} vai custar R${total:.2f} no final')


        elif opcao == 3:
            total = preco
            parcela = total / 2
            print(f'sua compra será parcelada em 2x de R${parcela:.2f} SEM JUROS')
            print(f'sua compra de R${preco:.2f} vai custar R${total:.2f} no final')

        elif opcao == 4:
            total = preco + (preco * 20/100)
            total_parcela = int(input('quantas parcelas?: '))
            parcela = total / total_parcela
            print(f'sua compra será parcelada em {total_parcela}x de R${parcela:.2f} COM JUROS')
            print(f'sua compra de R${preco:.2f} vai custar R${total:.2f} no final')


while True:
    resp = str(input('quer rodar? [S/N]: ')).strip().upper()
    if resp in 'Ss':
        programa_preco()
    else:
        break