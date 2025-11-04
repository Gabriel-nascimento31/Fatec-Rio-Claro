n = int(input('Digite um número: '))
for i in range(1, n + 1):
    linha_atual = ""
    for j in range(1, i + 1):
        linha_atual = linha_atual + str(j)
    print(linha_atual)
    