#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

l = float(input('Qual a largura da sua parede em metros? '))
h = float(input('Qual a altura da sua parede em metros? '))
a = l * h
print('Sabendo que a parede tem {}m², a quantidade de tinta necessária será de {:.1f}l'.format(a, a / 2))