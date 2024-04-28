#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))
menor = min(num1, num2, num3)
maior = max(num1, num2, num3)
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))

#num1 = int(input('Digite o primeiro número: '))
#num2 = int(input('Digite o segundo número: '))
#num3 = int(input('Digite o terceiro número: '))
#menor = num1
#if num2 < num1 and num2 < num3:
    #menor = num2
#if num3 < num1 and num3 < num2:
    #menor = num3
#maior = num1
#if num2 > num1 and num2 > num3:
    #maior = num2
#if num3 > num1 and num3 > num2:
    #maior = num3
#print('O menor valor digitado foi {}'.format(menor))
#print('O maior valor digitado foi {}'.format(maior))

#num1 = int(input('Digite o primeiro número: '))
#num2 = int(input('Digite o segundo número: '))
#num3 = int(input('Digite o terceiro número: '))
#if (num1 > num2 and num1 > num3) and (num2 < num3):
    #print('O maior número é {}, e o menor é {}'.format(num1, num2))
#elif (num2 > num1 and num2 > num3) and (num3 < num1):
    #print('O maior número é {}, e o menor é {}'.format(num2, num3))
#else:
    #print('O maior número é {}, e o menor é {}'.format(num3, num1))