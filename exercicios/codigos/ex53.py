# crie um programa que leia uma frase qualquer e digaa se ela é  um polindromo, desconsiderando os espaços
frase = str(input('digite qualquer coisa: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print(f'o inverso de {junto} é {inverso}')
if inverso == junto:
    print('temos um polimdromo')
else:
    print('não temos um polimdromo')