#Crie um programa que leia o nome completo de uma pessoa e mostre:
#– O nome com todas as letras maiúsculas e minúsculas.
#– Quantas letras ao todo (sem considerar espaços).
#– Quantas letras tem o primeiro nome.1

nome = str(input('Digite seu nome completo: ')).strip()
print('O nome em letras minúsculas é {}'.format(nome.upper()))
print('O nome em letras minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e tem {} letras'.format(separa[0], len(separa[0])))

#---RETIRANDO AS LINHAS 5 E 6---
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))