#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

from datetime import date
ano_nascimento = int(input('Em qual ano você nasceu? '))
if ano_nascimento == 0:
    ano_nascimento = date.today().year
if ano_nascimento % 4 == 0 and ano_nascimento % 100 != 0 or ano_nascimento % 400 == 0:
    print('Legal! Você nasceu em mu ano bissexto')
else:
    print('Você não nasceu em um ano bissexto')