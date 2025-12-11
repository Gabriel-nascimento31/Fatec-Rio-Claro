lista = []
for l in range(8):
    numeros = int(input('Digite um número inteiro: '))
    lista.append(numeros)
print(lista)
numero = int(input('Digite um número, para verificar quantas vezes ele aparece na lista: '))
qtd_vezes_aparece_lista = lista.count(numero)
print(f'O número {numero} aparece {qtd_vezes_aparece_lista} vezes na lista')
