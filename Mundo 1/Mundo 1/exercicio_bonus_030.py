#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

distancia_viagem = int(input('Em Km, qual será a distância da sua viagem? '))
preco1_viagem = distancia_viagem * 0.50
preco2_viagem = distancia_viagem * 0.45
if distancia_viagem <= 200:
    print('O preço da sua passagem será de R$ {}'.format(preco1_viagem))
else:
    print('O preço da sua passagem será de R$ {}'.format(preco2_viagem))