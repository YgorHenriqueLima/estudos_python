from time import sleep

nome = str(input('digite um nome completo: ')).strip()
print('Analisando seu nome...')
sleep(0.5)
print(f'seu nome em maiusculo é {nome.upper()}')
print(f'seu nome em minusculo é {nome.lower()}')
print('seu nome tem ao todo {} letras'.format(len(nome)))
separa = nome.split()
print(f'seu primeiro nome é {separa[0]} e ele tem {len(separa[0])} letras')
