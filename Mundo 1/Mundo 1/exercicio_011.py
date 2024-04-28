nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
print('A sua média foi {:1}'.format(media))
if media >= 6:
    print('Sua média foi boa. Parabéns!')
else:
    print('Sua média foi insuficiente. Estude mais!')

#print('PARABÉNS' if media >= 6 else 'ESTUDE MAIS')