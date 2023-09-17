# crie um programa que leia a idade e o sexo de várias pessoas. a cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar no final, mostre:

# A) quantas pessoas tem mais de 18 anos
# B) quantos homens foram cadastrados
# C) quantas mulheres com menos de 20 anos
tot18 = toth = totmulher20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('sexo[M/F]: ')).strip().upper()[0]

    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        toth += 1
    if sexo == 'F' and idade < 20:
        totmulher20 += 1

    resp = ' '
    while resp not in 'SN':
        resp = str(input('quer continuar[S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break

print(f'total de pessoa com mais de 18 anos: {tot18}')
print(f'ao todo temos {toth} homens cadastrados')
print(f'e temos {totmulher20} mulher(es) com menos de 20 anos')