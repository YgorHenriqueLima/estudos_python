# estrutura de repetição while / enquanto
from time import sleep

def contar():
    cont = 10
    while cont >= 0:  
        print(cont)
        cont -= 1
    print('terminei de contar')


def contar_interativo():
    cont = 0
    valor = int(input(' quer contar até quanto?: '))
    passo = int(input('e de quanto em quanto?: '))
    while cont <= valor:
        print(cont)
        cont += passo


def SomadorNumerico():
    cont = 1
    S = 0
    while cont <= 5:
        N = int(input(f'digite o {cont} valor: '))
        S += N
        cont += 1
    print(f'a soma dos resultados foram {S}')
    
SomadorNumerico()
def conversordolar():
    C = 1
    Q = int(input('quantas conversões?: '))
    while C <= Q:
        R = float(input('qual o valor em R$: '))
        D = R/4.74
        print(f'o valor convertido em US$ é: {D:.2f}')
        C += 1

def contageminteligente():
    print('CONTAGEM INTELIGENTE')
    print('-'*20)
    i = int(input('inicio: '))
    f = int(input('fim: '))
    print('-'*20)
    print('C O N T A N D O')
    sleep(1)

    while i <= f:
        print(i)
        i += 1

    if i >= f:
        while i >= f:
            print(i)
            i -= 1

def contagem_escola():

    print('-'*30)
    print('ESCOLA SANTA PACIÊNCIA')
    print('-'*30)

    # area das variaveis
    maior = 0
    cont = 1
    melhor_aluno = str

    Qalunos = int(input('quantos alunos a turma tem?: '))
    while cont <= Qalunos:

        print('------------------------')
        aluno = str(input(f'Aluno °{cont}: '))
        nota = float(input('Nota: '))
        print('------------------------')

        cont += 1

        if nota > maior:
            maior = nota
            melhor_aluno = aluno
    print(f'o aluno com melhor desempenho foi: {melhor_aluno} com nota de {maior}')

