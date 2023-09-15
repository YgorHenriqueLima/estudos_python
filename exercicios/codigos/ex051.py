#desenvolva um programa que leia o primeiro termo e na razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão
a1 = int(input('primeiro termo: '))
r = int(input('razão: '))
An = a1 + (10 - 1)*r
for c in range(a1, An+r, r):
    print(f'{c}', end=' =>')
print('fim')