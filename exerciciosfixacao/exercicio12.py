temperatura = int(input('Digite uma temperatura em Celsius: '))
if temperatura <= 15:
    print('FRIO')
elif 16 <= temperatura <= 25:
    print('AGRADÁVEL')
else:
    print('QUENTE')
    