#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

entrada = input('Digite um nome: ')
print(type(entrada))
print(entrada.isalnum())
print(entrada.isalpha())
print(entrada.isascii())
print(entrada.isdecimal())
print(entrada.isdigit())
print(entrada.isidentifier())
print(entrada.islower())
print(entrada.isnumeric())
print(entrada.isspace())
print(entrada.__init_subclass__())