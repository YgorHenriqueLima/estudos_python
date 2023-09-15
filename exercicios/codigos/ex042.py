def lin():
    print('-='*30)

lin()
print('analisador de triângulos')
lin()

def Triangulo():
    R1 = int(input('primeiro segmento: '))
    R2 = int(input('segundo segmento: '))
    R3 = int(input('terceiro segmento: '))
    if R1 < R2 + R3 and R2 < R1 + R3 and R3 < R1 + R2:
        print('os segmentos acima podem formar triangulos')
        if R1 == R2 == R3:
            print('é EQUILÁTERO')
        elif R1 != R2 != R3:
            print('é escaleno')
        else:
            print('é ISÓSCELES')
    else:
        print('os segmentos acima não podem formar um triângulo')


while True:
    resp = str(input('quer rodar? [S/N]: ')).strip().upper()
    if resp in 'Ss':
        Triangulo()
    else:
        break