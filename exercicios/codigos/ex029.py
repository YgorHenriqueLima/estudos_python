# escreva um programa que leia a velocidade de um carro
# se ele ultrapassar 80km/h mostre uma mensagem dizendo que ele foi multado
# a multa vai custar R$7,00 por cada km acima do limite

velocidade = float(input('qual é a velocidade do carro: '))
if velocidade > 80:
    print('você foi multado, porque excedeu o limite permitido')
    multa = (velocidade - 80) * 7
    print(f'você deve pagar uma multa de {multa:.2f}')
    print('cuidado, com a velocidade acima do permitido pode acabar com sua vida e com os outros :( ')
else:
    print(f'sua velocidade de {velocidade}km está na velocidade correta, tenha um bom dia e dirija com segurança :)')