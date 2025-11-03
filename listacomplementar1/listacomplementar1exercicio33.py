lista = []
for l in range(5):
    numero = int(input('Digite um número: '))
    lista.append(numero)
media = sum(lista) / len(lista)
print(f'A média é {media}')
