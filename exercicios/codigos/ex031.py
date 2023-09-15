distancia = float(input('qual a distância da sua viagem: '))
print(f'você estar prestes a começar a viagem de {distancia}km')
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print(f'e o preço da sua passagem será de R${preco:.2f}')