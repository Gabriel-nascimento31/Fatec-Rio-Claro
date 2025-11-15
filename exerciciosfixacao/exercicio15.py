idade = int(input('Digite a sua idade: '))
cartao = str(input('Você tem carteira de estudante (sim/não): '))
if idade < 6 or idade > 65:
    print('Sua tarifa de ônibus será grátis ')
elif cartao.lower() == "sim":
    print('Por você ser estudante você terá 50% de desconto na sua tarifa ')
else:
    print('Tarifa normal ')



            