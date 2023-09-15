num = int(input('digite um numero: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('analisando o valor')
print(f'''
          Unidade {u},
          dezena: {d},
          centena: {c},
          milhar: {m}
''')