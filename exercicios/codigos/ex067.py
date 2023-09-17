# faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. o programa será interrompido quando o numero solicitado for negativo 

while True:
    print('-='*20)
    n = int(input('quer ver a tabuada de qual valor?: '))
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
print('fim')

