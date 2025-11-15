saque = int(input('Digite o valor que você deseja sacar: R$ '))
notas100 = saque // 100
resto = saque % 100

notas50 = resto // 50
resto = resto % 50

notas20 = resto // 20
resto = resto % 20

notas10 = resto // 10

print('Notas de 100: {}' .format(notas100))
print('Notas de 50: {}' .format(notas50))
print('Notas de 20: {}' .format(notas20))
print('Notas de 10: {}' .format(notas10))



