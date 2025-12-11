lista = []
while True:
    numero = int(input('Digite um número, caso queira sair digite um número negativo : '))
    if numero >= 0:
        lista.append(numero)
        media = sum(lista) / len(lista)
    else:
        break
print(f'A média é {media}')




