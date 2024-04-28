#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

r = float(input('Digite quanto em R$ você tem: '))
print('Convertando para a moeda americana, você terá US$ {:.2f}'.format(r / 3.27))