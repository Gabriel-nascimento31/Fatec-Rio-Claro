nota = float(input('Digite uma nota entre 0 e 10: '))
if nota < 0 or nota > 10:
    print('Nota inválida! Digite uma nota de 0 a 10! ')
elif 9 <= nota <= 10:
    print('Sua nota é A! ')
elif 7 <= nota <= 8.9:
    print('Sua nota é B! ')
elif 5 <= nota <= 6.9:
    print('Sua nota é C! ')
elif 3 <= nota <= 4.9:
    print('Sua nota é D! ')
else:
    print('Sua nota é E! ')
