#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

from math import sqrt
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
print('O valor da hipotenusa será {:.2f}'.format(sqrt((co ** 2) + (ca ** 2))))