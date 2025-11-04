qtd_alunos = int(input('Digite a quantidade de alunos: '))
aprovados = 0
reprovados = 0
for a in range(qtd_alunos):
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    media = (nota1 + nota2) / 2
    print(media)  
    if media >= 6:
        aprovados = aprovados + 1
    else:
        reprovados = reprovados + 1
print(f'{aprovados} aprovados ')
print(f'{reprovados} reprovados ')


