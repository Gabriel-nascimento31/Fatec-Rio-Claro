trabalho_laboratorio = float(input('Digite a nota do trabalho de laboratório: '))
avaliacao_semestral = float(input('Digite a nota da avaliação semestral: '))
exame_final = float(input('Digite a nota do exame final: '))
media_ponderada = ((trabalho_laboratorio * 2) + (avaliacao_semestral * 3) + (exame_final * 5)) / 10
print(f'A média ponderada do aluno é {media_ponderada} ')
if 10.0 >= media_ponderada >= 8.0:
    print('NOTA: A')
elif 7.9 >= media_ponderada >= 7.0:
    print('NOTA: B')
elif 6.9 >= media_ponderada >= 6.0:
    print('NOTA: C')
elif 5.9 >= media_ponderada >= 5.0:
    print('NOTA: D')
elif 4.9 >= media_ponderada >= 0.0:
    print('NOTA: E')


