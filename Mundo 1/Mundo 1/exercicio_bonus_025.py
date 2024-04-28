#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

# --STRIP() RETIRA OS ESPAÇOS VAZIOS DA DIREITA E ESQUERDA--#
frase = str(input('Digite uma frase: ')).strip()
frase_maiuscula = frase.upper()
print('Nessa frase, a letra "A" aparece {} vezes'.format(frase_maiuscula.count('A')))
print('A letra "A" aparece pela inicialmente na posição {}'.format(frase_maiuscula.find('A') + 1 ))
print('E aparece por último na posição {}'.format(frase_maiuscula.rfind('A')))
