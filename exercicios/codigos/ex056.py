# desenvolva um programa que leia o nome, idade e sexo de 4 pessoas
# no final mostre:
    # a media de idade do grupo
    # qual é o nome do homem mais velho
    # quantas mulheres tem menos de 20 anos


# as variaveis principais
soma_idade = 0
media_idade = 0
nome_velho = ''
maior_idade_homem = 0
tot_mulher_com_20 = 0


# primeiro o nome, idade e sexo das pessoas
for p in range(1, 5):

    print(f'---{p}°pessoa---')
    nome = str(input('nome: '))
    idade = int(input('idade: '))
    sexo = str(input('sexo[M/F]: ')).strip().upper()

    # aqui será salvado/acrescentado as idade
    soma_idade += idade

    # se a primeira pessoa que tiver o sexo masculino for maior de idade, o nome dele aparecerá 
    if p == 1 and sexo in 'Mm':
        maior_idade_homem = idade
        nome_velho = nome

    # se o sexo for masculino e a idade for a maior idade, o nome dele aparecerá
    if sexo in 'Mm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_velho = nome

    # se o sexo for feminino e idade for menor que 20, o total de mulheres com menos de 20 anos vai ser por parte do programa e dos resultados obtidos
    if sexo in 'Ff' and idade < 20:
        tot_mulher_com_20 += 1



media_idade = soma_idade / 4
print(f'''a media de idade do grupo é de {media_idade}\no homem mais velho tem {maior_idade_homem} anos e seu nome é {nome_velho}\nao todo são(é) {tot_mulher_com_20} mulheres com menos de 20 anos''')