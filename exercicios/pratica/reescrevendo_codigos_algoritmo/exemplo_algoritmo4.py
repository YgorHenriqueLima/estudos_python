# condições if e else

#----------------------------------------------------------------------------------------------------
def AnaliseIdade():
    ano = int(input('em que ano estamos: '))
    nasc = int(input('data de nascimento: '))
    idade = ano - nasc
    print(f'em {ano} você terá {idade} anos')
    if idade >= 21:
        print(' e você já terá atingido a maioridade')
    else:
        print(f' e você ainda é jovem')

# ----------------------------------------------------------------------------------------------------
def ParOuImpar():
    N = int(input('digite o numero: '))
    if N % 2 == 0:
        print(f'o numero {N} é par')
    else:
        print(f'o numero {N} é impar')


# -----------------------------------------------------------------------------------------------------
def CalcIMC():
    M = float(input('Massa (KG): '))
    A = float(input('Altura (M): '))
    IMC = M / (A**2)
    print(f"IMC: {IMC:.5f}")
    if (IMC >= 18.5) and (IMC < 25):
        print(f'parabéns, você está no seu peso ideal ')


def Nota():
    n1 = float(input('primeira nota: '))
    n2 = float(input('segunda nota: '))
    media = (n1 + n2) / 2
    if media >= 6.0:
        print('aprovado')
    else:
        print('reprovado')


    