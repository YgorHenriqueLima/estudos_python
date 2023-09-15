n1 = float(input('primeira nota: '))
n2 = float(input('segunda nota: '))
media = (n1 + n2) / 2
situacao = ['\033[33mrecuperacao\033[33m', '\033[31mreprovado\033[31m', '\033[32maprovado\033[32m']

if 7 > media >= 5.0:
    print(f'''media: {media}
situação: {situacao[0]}''')

elif media < 5.0:
    print(f'''media {media}
situação: {situacao[1]}''')

elif media >= 7.0:
    print(f''' media: {media}
situação: {situacao[2]}''')