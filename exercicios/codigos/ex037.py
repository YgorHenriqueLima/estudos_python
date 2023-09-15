num = int(input('digite um numero inteiro: '))
print("""escolha uma das bases para conversão:
       [ 1 ] converter para binário
       [ 2 ] converter para octal
       [ 3 ] converter para Hexadecimal""")
opcao = int(input('digite sua opcao: '))
if opcao == 1:
    print(' {} convertendo para binario o valor é {}'.format(num, bin(num)[2:]))

elif opcao == 2:
    print('{} convertendo para octal o valor é {}'.format(num, oct(num)[2:]))

elif opcao == 3:
    print('{} convertendo para binario o valor é {}'.format(num, hex(num)[2:]))
else:
    print('opção inválida tente novamente')