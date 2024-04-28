#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

n1 = float(input('Digite a pontuação da AV1: '))
n2 = float(input('Digite a pontuação da AV2: '))
m = (n1 + n2) / 2
print('A média simples das notas {} e {} vale {:.2f}'.format(n1, n2, m))