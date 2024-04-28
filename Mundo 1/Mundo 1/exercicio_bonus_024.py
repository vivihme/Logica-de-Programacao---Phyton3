#Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

# --STRIP() RETIRA OS ESPAÇOS VAZIOS DA DIREITA E ESQUERDA--#
nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome tem Silva? {}'.format('SILVA' in nome.upper()))