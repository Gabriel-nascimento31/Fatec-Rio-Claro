idade = int(input('Digite a sua idade: '))
deficiente = input('Você é deficiente (sim/não): ').lower() 
gestante = input('Você é gestante (sim/não): ').lower()
if idade >= 60 or deficiente == "sim":
    print('Seu atendimento é de prioridade máxima ')
elif gestante == "sim":
    print('Seu atendimento é de priporidade média ')
else:
    print('Seu atendimento será normal ')
    