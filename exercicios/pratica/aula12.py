nome = str(input('digite seu nome: '))
if nome == 'Ygor':
    print('que nome bonito')

elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('seu nome é bem popular no Brasil')

elif nome in 'Ana Claudia Jéssica Juliana':
    print('belo nome feminino')

elif nome in 'João Gustavo':
    print('belo nome conhecido masculino')
else:
    print('seu nome é bem normal')

print(f'bom dia {nome}')