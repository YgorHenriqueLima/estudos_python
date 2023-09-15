n1 = float(input('primeira nota do aluno: '))
n2 = float(input('segunda nota do aluno: '))
media = (n1 + n2) / 2
print(f'a sua média foi: {media}')
if media > 6.0:
    print('sua nota foi aprovada :)')
else:
    print('sua nota foi reprovada :(')