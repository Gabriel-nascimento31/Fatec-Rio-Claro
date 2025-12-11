salario_bruto = float(input('Digite o seu salário bruto: R$ '))
if salario_bruto <= 2112.00:
    print('Você não tem imposto de renda a pagar.')
elif salario_bruto <= 2826.65:
    imposto_renda = (salario_bruto * 7.5 / 100) - 158.40
    print(f'Você tem R${imposto_renda:.2f} de desconto de imposto de renda.')
elif salario_bruto <= 3751.05:
    imposto_renda = (salario_bruto * 15 / 100) - 370.40
    print(f'Você tem R${imposto_renda:.2f} de desconto de imposto de renda.')
elif salario_bruto <= 4664.68:
    imposto_renda = (salario_bruto * 22.5 / 100) - 651.73
    print(f'Você tem R${imposto_renda:.2f} de desconto de imposto de renda.')
else:
    imposto_renda = (salario_bruto * 27.5 / 100) - 884.96
    print(f'Você tem R${imposto_renda:.2f} de desconto de imposto de renda.')

    