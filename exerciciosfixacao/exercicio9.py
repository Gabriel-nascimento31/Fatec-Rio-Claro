salario = float(input('Digite o seu salário atual: '))
if salario < 2000:
    print('Você receberá um bônus de 20% do seu salário!')
    bonus = (salario * 20 / 100) + salario
    print('Seu salário com o bônus ficará R${:.2f}' .format(bonus))
elif 2000 <= salario <= 5000:
    print('Você receberá um bônus de 10% do seu salário!')
    bonus = (salario * 10 / 100) + salario
    print('Seu salário com o bônus ficará R${:.2f}' .format(bonus))
else:
    print('Você receberá um bônus de 5% do seu salário! ')
    bonus = (salario * 5 / 100) + salario
    print('Seu salário com o bônus ficará R${:.2f}' .format(bonus))
    
