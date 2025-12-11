lista = []
for l in range(6):
    n = float(input('Digite um número real: '))
    lista.append(n)
media = sum(lista) / len(lista)
print(f'MÉDIA = {media}')
