n = int(input('Digite um número (n) para somar apenas os ímpares de 1 até n: '))
soma_impares = 0
for numero in range(1, n + 1):
    if numero % 2 != 0:
        soma_impares = soma_impares + numero
print(soma_impares)
