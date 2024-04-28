#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

# --STRIP() RETIRA OS ESPAÇOS VAZIOS DA DIREITA E ESQUERDA--#
nome = str(input('Digite seu nome completo: ')).strip()
nome_dividido = nome.split()
print('Seu primeiro nome é {}'.format(nome_dividido[0]))
print('Seu último nome é {}'.format(nome_dividido[len(nome_dividido)-1]))