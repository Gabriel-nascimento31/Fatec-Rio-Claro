alunos = ['aluno1', 'aluno2', 'aluno3', 'aluno4', 'aluno5', 'aluno6']
for aluno in alunos:
    nota1 = float(input('Digite a nota 1: '))
    nota2 = float(input('Digite a nota 2: '))
    media = (nota1 + nota2) / 2
    print(f'Média = {media}')
    if media <= 3:
        print('REPROVADO')
    elif media <= 7:
        print('EXAME')
    else:
        print('APROVADO') 



    