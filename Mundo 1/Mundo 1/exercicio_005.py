#FAÇA UM PROGRMA QUE LEIA DOIS NÚMEROS E MOSTRE OS RESULTADOS PARA SOMA, SUBTRAÇÃO, MULTIPLICAÇÃO, DIVISÃO, DIVISÃO INTEIRA, EXPONENCIAÇÃO E O RESTO DE DIVISÃO

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
so = n1 + n2
su = n1 - n2
m = n1 * n2
e = n1 ** n2
d = n1 / n2
di = n1 // n2
r = n1 % n2
print('A soma é {}. A subtração vale {}. A multiplicação, {}'.format(so, su, m))
print('A exponenção tem valor de {}, enquanto a divisão é {:.3f}, e a divisão inteira, {}'.format(e, d, di))
print('O resto da divisão é {}'.format(r))
