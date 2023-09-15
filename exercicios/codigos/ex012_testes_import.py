from math import sqrt, ceil, hypot, sin, cos, tan, radians, trunc
from random import choice, shuffle
from random import randint



def lersqrt():
    num = int(input('digite um numero: '))
    raiz = sqrt(num)
    print(f'a raiz de {num} é igual a {ceil(raiz)}')

def randomico():
    num = randint(1, 10)
    print(num)

def quebraNumero():
    '''num = float(input('digite um valor: '))
    print(f'o valor digitado foi {num} e a porção inteira é {trunc(num)}')'''
    num = float(input('digite um valor: '))
    print(f'o valor digitado foi {num} e a porção inteira é {int(num)}')

def cat_hipotenusa():
    co = float(input('comprimento do cateto oposto: '))
    ca = float(input('comprimento do cateto adijacente: '))
    hi = hypot(co, ca)
    print(f'a hipotenusa vai medir {hi:.2f}')

def seno_coss_tangen():
    angulo = float(input('digite o angulo que você deseja: '))
    seno = sin(radians(angulo))
    print(f'o angulo de {angulo} tem o seno de {seno:.2f}')
    cosseno = cos(radians(angulo))
    print(f'o angulo de {angulo} tem o cosseno de {cosseno:.2f}')
    tangente = tan(radians(angulo))
    print(f'o angulo de {angulo} tem o tangente de {tangente:.2f}')


def escolhaaluno():
    n1 = str(input('Primeiro aluno: '))
    n2 = str(input('Segundo aluno: '))
    n3 = str(input('Terceiro Aluno: '))
    n4 = str(input('Quarto Aluno: '))
    lista = [n1, n2, n3, n4]
    escolhido = choice(lista)
    print(f'o aluno escolhido foi {escolhido}')


escolhaaluno()