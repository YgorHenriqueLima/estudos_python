# simule o funcionamento de um caixa eletronico
# perginte ao usuário o valor a ser sacado (numero inteiro)
# informar quantas cédulas de cada valor serão entregues

# OBS: considere que o CAIXA possui cédulas de R$50, R$20, R$10, R$1

print('-='*30)
print('BANCO DO CEV')
print('-='*30)
valor = int(input('valor a ser sacado: '))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'total de {totced} de {ced}')
        if total == 50:
            ced = 20
        elif total == 20:
            ced = 10
        elif total == 10:
            ced = 1
        elif total == 0:
            break
