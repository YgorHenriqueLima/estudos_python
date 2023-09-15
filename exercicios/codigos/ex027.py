from time import sleep

n = str(input('digite seu nome completo: '))
nome = n.split()
sleep(1)
print('muito prazer em te conhecer!')
print('seu primeiro nome é {}'.format(nome[0]))
print('seu ultimo nome é {}'.format(nome[len(nome)-1]))
