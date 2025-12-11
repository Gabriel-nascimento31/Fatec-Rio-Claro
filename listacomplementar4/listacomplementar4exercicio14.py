lista_positivos = []
lista_negativos = []
for c in range(10):
    numero = int(input('Digite um número: '))
    if numero > 0:
        lista_positivos.append(numero)
    else:
        lista_negativos.append(numero)
print(lista_positivos)
print(lista_negativos)
