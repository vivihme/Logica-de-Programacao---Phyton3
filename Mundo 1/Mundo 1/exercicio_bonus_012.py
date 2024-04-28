#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

s = float(input('Qual o seu salário? '))
print('Seu novo salário será de {:.1f}'.format(s + (s * 0.15)))