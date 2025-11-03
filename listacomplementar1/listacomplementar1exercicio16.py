nota = float(input('Digite a nota do aluno: '))
if nota > 10 or nota < 0:
    print('NOTA INVÁLIDA! Digite uma nota de 0 a 10 ') 
elif nota >= 7:
    print('APROVADO ')
else:
    print('REPROVADO ')

