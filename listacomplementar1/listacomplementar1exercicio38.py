n = int(input('Digite um número (n) para exibir a quantidade de números entre 1 e n que são múltiplos de 7: '))
multiplos_de_7 = 0
for numero in range(1, n + 1):
    if numero % 7 == 0:
        multiplos_de_7 = multiplos_de_7 + 1
print(multiplos_de_7)
