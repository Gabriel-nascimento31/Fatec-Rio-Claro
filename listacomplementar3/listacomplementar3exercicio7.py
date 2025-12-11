from math import factorial
n = int(input('Digite a quantidade de números que você quer ver o fatorial: '))
for e in range(n):
    numero = int(input('Digite um número: '))
    fatorial = factorial(numero) 
    print(fatorial)


