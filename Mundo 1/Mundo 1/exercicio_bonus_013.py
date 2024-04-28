#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

tc = float(input('Digite a temperatura em ºC: '))
tf = (tc * 1.8) + 32
print('A temperatura equivale a {:.1f}ºF'.format(tf))