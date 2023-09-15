# melhore o anterior, perguntando o usuário se ele quer mostrar mais alguns temos, o programa encerra quando ele disser que quer mostrar o termos
print('gerador de pa')

print('-='*10)
a1 = int(input('primeiro termo: '))
razao = int(input('razão: '))
print('-='*10)

termo = a1
cont = 1
total = 0
# o programa começa com 10 termos, só depois que o usuário vaai poder digitar 
mais = 10

# isto é quando o usuário digitar 0 quer dizer que ele quer sair do programa
while mais != 0:
    # o total a ser mostrado vai ser o total que está com 0 acrescentando quantos termos a mais o usuário vai querer
    total = total + mais
    while cont <= total:
        print(f'{termo} ->', end=" ")
        termo += razao
        cont += 1
    print("PAUSA")
    mais = int(input('quantos termos você quer mostrar a mais?: '))
    print(f"progressão finalizada com {total} termos mostrados")