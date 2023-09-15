#faca um programa que leia o sexo da pessoa, mas só aceita os valores "M" ou "f" caso esteja errado, peça a digitação novamente até ter um valor correto
nome = str(input('digite seu nome: '))
sexo = str(input('digite seu sexo [M/F]: ')).strip().upper()
while sexo not in 'MmFf':
    sexo = str(input('dados inválidos, digite novamente seu sexo [M/F]: ')).strip().upper()
print(f'nome {nome} e sexo {sexo} foram registrados com sucesso')
