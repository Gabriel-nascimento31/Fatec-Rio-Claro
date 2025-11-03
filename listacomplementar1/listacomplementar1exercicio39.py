n = int(input('Digite um número (n) para exibir a tabuada de todos os números de 1 até n: '))
for tabuada in range(1, n + 1):
    print(f'\n--- Tabuada do {tabuada} ---')
    for multiplicador in range(1, 11):
        resultado = tabuada * multiplicador
        print(f'{tabuada} x {multiplicador} = {resultado}')
        