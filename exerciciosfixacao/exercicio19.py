idade = int(input('Digite sua idade: '))
if idade <= 12:
    print('CATEGORIA INFANTIL')
elif 13 <= idade <= 17:
    print('CATEGORIA JUVENIL')
elif 18 <= idade <= 40:
    print('CATEGORIA ADULTO')
else:
    print('CATEGORIA VETERANO')
    