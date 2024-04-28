# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = int(input('Qual o seu salário? '))
if salario > 1250:
    print('Seu novo salário será de R$ {}, um aumento de 10%'.format(salario + (salario * 0.1)))
else:
    print('Seu novo salário será de R$ {}, um aumento de 15%'.format(salario + (salario * 0.15)))