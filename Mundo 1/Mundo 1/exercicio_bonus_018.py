#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

from random import choice
a1 = str(input('Digite o nome do primeiro estudante: '))
a2 = str(input('Digite o nome do segundo estudante: '))
a3 = str(input('Digite o nome do terceiro estudante: '))
a4 = str(input('Digite o nome do quarto estudante: '))
choice = choice([a1, a2, a3, a4])
print('O estudante escolhido foi {}'.format(choice))