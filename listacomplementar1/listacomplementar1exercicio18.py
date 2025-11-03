nota1 = float(input('Digite a nota do aluno: '))
nota2 = float(input('Digite a nota do aluno: '))
nota3 = float(input('Digite a nota do aluno: '))
media = (nota1 + nota2 + nota3) / 3
if media >= 7:
    print(f'MÉDIA = {media:.1f} ')
    print('APROVADO ')
else:
    print(f'MÉDIA = {media:.1f} ')
    print('REPROVADO ')

          