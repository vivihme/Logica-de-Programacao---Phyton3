# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep
computador = randint(0,5)
jogo = int(input('Pensei em um número de 0 a 5. Tente adivinhar: '))
print('PROCESSANDO...')
sleep(3)
if jogo == computador:
    print('Você é fera! Realmente eu pensei no número {}'.format(computador))
else:
    print('Venci! Eu pensei no número {}, não no {}'.format(computador, jogo))