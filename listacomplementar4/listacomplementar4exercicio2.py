lista = []
for e in range(8):
    numero = int(input('Digite um número: '))
    lista.append(numero)
    maior = max(lista)
    menor = min(lista)
print(f'O maior valor da lista é {maior} ')
print(f'O menor valor da lista é {menor} ')
