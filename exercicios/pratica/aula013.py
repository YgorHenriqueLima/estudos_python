# aula 13 do curso em vídeo python
# exemplos de códigos de estrutura de repetição

def contagem_normal():
    for c in range(1, 7):
        print(c)
    print('fim')

def contagem_ao_contrário():
    for c in range(6, 0, -1):
        print(c)
    print('fim')


def contar_pulando_dois_em_dois():
    for c in range(0, 7, 2): # isto é, o 0 seria o inicio, o 7 o final, e o 2 seria pulando de 2 em 2
        print(c)
    print('fim')

def exemplo_contagem1():
    n = int(input('digite um valor: '))
    for c in range(0, n+1):
        print(c)
    print('fim')

def exemplo_contagem2():
    i = int(input('inicio: '))
    f = int(input('final: '))
    p = int(input('passo: '))
    for c in range(i, f+1, p):
        print(c)
    print('fim')

def exemplo_contagem3():
    s = 0
    for c in range(0, 4):
        n = int(input('digite um valor: '))
        s += n
    print(f'o somatório de todos os valores foi {s}')