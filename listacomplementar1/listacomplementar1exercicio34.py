lista = []
qtd_pares = 0

for c in range(10):
    numero = int(input('Digite um número: '))
    lista.append(numero)
    if numero % 2 == 0:
        qtd_pares = qtd_pares + 1
print(f'A quantidade de pares é {qtd_pares}')
    