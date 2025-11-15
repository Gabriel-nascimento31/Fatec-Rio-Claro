bruto = float(input('Digite o seu salário bruto: '))
if bruto <= 1900:
    print('Você está isento de imposto de renda! ')
elif 1901 <= bruto <= 2800:
    desconto = bruto - (bruto * 7.5 / 100)
    print('Você terá um desconto de alíquota de imposto de renda de 7,5%, portanto seu salário liquido será de R${:.2f}' .format(desconto))
elif 2801 <= bruto <= 3700:
    desconto = bruto - (bruto * 15 / 100)
    print('Você terá um desconto de alíquota de imposto de renda de 15%, portanto seu salário liquido será de R${:.2f}' .format(desconto))
elif 3701 <= bruto <= 4600:
    desconto = bruto - (bruto * 22.5 / 100)
    print('Você terá um desconto de alíquota de imposto de renda de 22.5%, portanto seu salário liquido será de R${:.2f}' .format(desconto))
else:
    desconto = bruto - (bruto * 27.5 / 100)
    print('Você terá um desconto de alíquota de imposto de renda de 27.5%, portanto seu salário liquido será de R${:.2f}' .format(desconto))
    