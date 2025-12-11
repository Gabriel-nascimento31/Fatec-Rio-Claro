lista = []
for c in range(10):
    numero = int(input('Digite um número: '))
    lista.append(numero)
    conjunto = set(lista)
    lista2 = list(conjunto)
print(lista2)
