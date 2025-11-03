lista = []
qtd_positivos = 0
for c in range(10):
    numero = int(input('Digite um número: '))
    lista.append(numero)
    if numero > 0:
        qtd_positivos = qtd_positivos + 1
print(f'A quantidade de positivos é {qtd_positivos}')
