
x = []
soma = 0
quantidade_pares = 0
quantidade_impares = 0
for n in range(10):
    numero = int(input('Digite um número: '))
    x.append(numero)
    if numero % 2 == 0:
        soma = soma + numero
        quantidade_pares = quantidade_pares + 1
    else:
        quantidade_impares = quantidade_impares + 1
print(soma)
print(f'{quantidade_pares} Pares ')
print(f'{quantidade_impares} ÍMPARES ')
    

