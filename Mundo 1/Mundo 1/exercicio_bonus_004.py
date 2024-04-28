#Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.

ni = int(input('Digite um número inteiro: '))
print('O número inteiro informado é {}. Tem como sucesso o valor {}, e como antecessor o {}'.format(ni, ni + 1, ni - 1))