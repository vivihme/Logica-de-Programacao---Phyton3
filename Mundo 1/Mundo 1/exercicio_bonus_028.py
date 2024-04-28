#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = int(input('Em km/h, qual a velocidade exibida no tacógrafo do seu carro? '))
limite = 80
multa = (velocidade - limite) * 7
if velocidade > 80:
    print('A velocidade do seu carro estava {}km/h, isso é acima do limite permitido'.format(velocidade))
    print('A multa será de R$ {}'.format(multa))
else:
    print('A velocidade do seu carro está no limite permitido')