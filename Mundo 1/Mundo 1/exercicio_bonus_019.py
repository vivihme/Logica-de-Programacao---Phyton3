#O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle
a1 = str(input('Digite o nome do primeiro estudante: '))
a2 = str(input('Digite o nome do segundo estudante: '))
a3 = str(input('Digite o nome do terceiro estudante: '))
a4 = str(input('Digite o nome do quarto estudante: '))
alunos = [a1, a2, a3, a4]
shuffle(alunos)
alunos = ', '.join(alunos)
print(f'A lista de apresentação será {alunos}')

#--RETIRANDO AS LINHAS 8 E 9---
#print('A lista de apresentação será {}'.format(alunos))