#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

da = int(input('Por quantos dias você utilizou o carro? '))
kmp = float(input('Quantos kilômetros você percorreu? '))
pa = (da * 60) + (kmp * 0.15)
print('Considerando que você utilizou o carro por {} dia(s) e percorreu {:.2f}km, o total será R${:.2f}'.format(da, kmp, pa))