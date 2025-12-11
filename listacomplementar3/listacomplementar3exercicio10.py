lista = ['aluno1', 'aluno2', 'aluno3', 'aluno4', 'aluno5', 'aluno6', 'aluno7', 'aluno8', 'aluno9', 'aluno10']
qtd_homens = 0
qtd_mulheres = 0
for aluno in lista:
    idade = int(input('Digite a idade do aluno: '))
    sexo = input('Digite o sexo do aluno (M/F): ')
    if sexo == 'M':
        qtd_homens = qtd_homens + 1
        
    elif sexo == 'F':
        qtd_mulheres = qtd_mulheres + 1
print(f'{qtd_homens} HOMENS CADASTRADOS')
print(f'{qtd_mulheres} MULHERES CADASTRADAS')



