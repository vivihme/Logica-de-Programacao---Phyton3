#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import sin, cos, tan, radians
num = float(input('Digite o valor de um ângulo: '))
sen = sin(radians(num))
cos = cos(radians(num))
tan = tan(radians(num))
print('Este ânglo tem valor de seno {:.2f}, cosseno {:.2f} e tangente {:.2f}'.format(sen, cos, tan))