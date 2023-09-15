# faça um programa do ano de nascimento de um jovem, de acordo com sua idade:
# - se ele ainda vai se alistar ao serviço militar
# - se é a hora de se alistar
# - se já passou do tempo do alistamento
# o programa vai mostrar o tempo que falta ou que passou do prazo

import datetime

# analisar o ano atual
atual = datetime.date.today().year

# perguntando qual o nome do usuario
print('-='*30)
print('EXERCITO BRASILEIRO')
print('-='*30)
print('''diga o seu sexo:
        [1] masculino
        [2] feminino
''')
sexo = int(input('digite aqui: '))
if sexo == 1:
    print("ALISTAMENTO OBRIGATÓRIO")
    nome = str(input('digite seu nome: ')).strip()
    nasc = int(input('ano de nascimento: '))
    idade = atual - nasc
    if idade == 18:
        print(f'jovem {nome} você tem que se alistar imediatamente')

    elif idade < 18:
        saldo = 18 - idade
        print(f'jovem {nome}, ainda faltam {saldo} anos para se alistar')
        ano = atual + saldo
        print(f'seu alistamento será em {ano}')

    elif idade > 18:
        saldo = idade - 18
        print(f'você já deveria ter se alistado há {saldo} anos')
        ano = atual - saldo
        print(f'seu alistamento foi em {ano}')

if sexo == 2:
    print('não é obrigatório se alistar, mas se quiser entrar para o exercito brasileiro, entre em contato conosco')




