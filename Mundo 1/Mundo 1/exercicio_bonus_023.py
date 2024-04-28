#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

#--STRIP() RETIRA OS ESPAÇOS VAZIOS DA DIREITA E ESQUERDA--#
cidade = str(input('Em qual cidade você nasceu? ')).strip()
print(cidade[:5] == 'Santo' or cidade[:5]== 'santo' or cidade[:5] == 'SANTO')

#--SOLUÇÃO DO GUSTAVO GUANABARA--#
#cid = str(input('Em qual cidade você nasceu? ')).strip()
#print(cid[:5].upper() == 'SANTO')