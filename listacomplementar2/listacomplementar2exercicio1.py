notas = int(input('Digite quantas notas você deseja calcular: '))
soma = 0
for t in range(notas):
    nota = int(input('Digite a nota: '))
    soma = soma + nota
media = soma/ notas
print(media)
if media >= 7:
    print('APROVADO')
else:
    print('REPROVADO')
