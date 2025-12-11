lista = []
for l in range(6):
    numero = int(input('Digite um número: '))
    lista.append(numero)
    for l in lista:
        invertida = lista[::-1]
print(invertida)

