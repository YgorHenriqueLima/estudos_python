#  REFAÇA O DESAFIO 009 MOSTRANDO A TABUADA DE UM NUMERO QUE O USUÁRIO ESCOLHER, SÓ QUE AGORA UTILIZANDO UM LAÇO FOR
def lin():
    print('')

def programa_tabuada():   
    print('''escolha a sua tabuada:
        [ 1 ] multiplicação
        [ 2 ] adição
        [ 3 ] subtração
    ''')
    opcao = int(input('qual a sua opção: '))

    n = int(input('digite a sua tabuada: '))
    i = int(input('inicio: '))
    f = int(input('final: '))

    if opcao == 1:
        for c in range(i, f):
            print(f'{n} x {c} = {n*c}')

    if opcao == 2:
        for c in range(i, f):
            print(f'{n} + {c} = {n+c}') 

    if opcao == 3:
        for c in range(i, f):
            print(f'{n} - {c} = {n-c}') 
       
while True:
    resp = str(input('quer rodar? [S/N]: ')).strip().upper()
    if resp in 'Ss':
        programa_tabuada()
    else:
        break