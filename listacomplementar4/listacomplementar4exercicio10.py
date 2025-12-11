
soma = 0
while True:
    numero = int(input('Digite um número, caso queira sair digite 0: '))
    if numero == 0:
        break
    else:
        soma = soma + numero
        
print(f'SOMA = {soma}')

