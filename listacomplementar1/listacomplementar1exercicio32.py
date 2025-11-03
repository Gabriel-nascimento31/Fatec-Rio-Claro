numeros = []
for k in range(5):
    numero = int(input('Digite um número: '))
    numeros.append(numero)
menor_numero = min(numeros)
print(f'O menor número é {menor_numero}')
