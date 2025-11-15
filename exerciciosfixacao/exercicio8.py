l1 = float(input('Digite um número: '))
l2 = float(input('Digite um número: '))
l3 = float(input('Digite um número: '))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Esses lados podem formar um triângulo! ')
    if l1 == l2 == l3:
        print('TRIÂNGULO EQUILÁTERO! ')
    elif l1 == l2 or l2 == l3 or l1 == l3:
        print('TRIÂNGULO ISÓSCELES! ')
    else:
        print('TRIÂNGULO ESCALENO ')
else:
    print('Os lados que você digitou não podem formar um triângulo! ')
    
    




