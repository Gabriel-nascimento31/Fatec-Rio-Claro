lista =[]
pares = 0
impares = 0

for x in range(10):
    n = int(input('Digite um número: '))
    lista.append(n)
    if n % 2 == 0:
        
        pares = pares + 1
    else:
        impares = impares + 1
print(f'{lista} ')
print(f'{pares} Pares')
print(f'{impares} Impares ')


