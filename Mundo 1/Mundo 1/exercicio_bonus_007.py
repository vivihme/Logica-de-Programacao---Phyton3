#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

d = float(input('Digite uma medida em metros: '))
dc = d * 100
dm = d * 1000
print('{:.0f} metros é igual a {:.0f}cm e {:.0f}mm'.format(d, dc, dm))