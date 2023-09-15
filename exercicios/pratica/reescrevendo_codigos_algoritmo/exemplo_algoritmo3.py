mai = 0
pesado = ""

def Topo():
    print("------------------------------")
    print("D E T E C T O R DE P E S A D 0")
    print(f"maior peso até agora {mai}")
    print("------------------------------")


i = 1
Topo()
for i in range(1, 5):
    n = str(input('digite seu nome: '))
    p = float(input(f'digite o peso de {n}: '))
    if p > mai:
        mai = p
        pesado = n
    Topo()
Topo()
print(f"a pessoa mais pesada é {pesado} com {mai} quilos")
    