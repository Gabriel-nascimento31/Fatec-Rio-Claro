lista = []
multiplicacao = 1
for c in range(5):
    numero = int(input('Digite um número: '))
    lista.append(numero)
    
    multiplicacao = multiplicacao * numero
print(f'MULTIPLICAÇÃO = {multiplicacao}')

