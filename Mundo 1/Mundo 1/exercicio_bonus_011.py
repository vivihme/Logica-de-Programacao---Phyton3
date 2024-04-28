#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

vp = float(input('Qual o valor desse produto em R$? '))
print('Na liquidção, esse produto terá 5% de desconto e sairá por {:.2f}'.format(vp - (vp * 0.05)))