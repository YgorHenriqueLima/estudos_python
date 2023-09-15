def IMC():
    peso = float(input('peso (kg): '))
    altura = float(input('altura (m): '))
    IMC = peso / (altura**2)
    print(f'seu peso foi {IMC}')

    # ABAIXO DO PESO
    if IMC <= 20.0:
        print('você está abaixo do peso \n o peso IMC ideal é entre 21 e 24.9')

    # PESO IDEAL
    elif 21.0 <= IMC <= 24.9: 
        print('você está no IMC ideal, PARABÉNS!')

    # OBESIDADE LEVE
    elif 25.0 <= IMC <= 29.9:
        print('você está com obesidade leve \n o IMC ideal é entre 21 e 24.9')

    # OBESIDADE MODERADA
    elif 30.0 <= IMC <= 39.9:
        print('você está com obesidade moderada \n o IMC ideal é entre 21 e 24.9')

    elif IMC >= 40:
        print('\033[31mcuidado! OBESIDADE MÓRBIDA, cuide-se\033[31m')



while True:
    resp = str(input('quer rodar? [S/N]: ')).strip().upper()
    if resp in 'Ss':
        IMC()
    else:
        break