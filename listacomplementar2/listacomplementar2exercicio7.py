altura = int(input('Digite a altura: '))
largura = int(input('Digite a largura: '))
print('*' * largura)  
for r in range(altura - 2):
    print('*' + ' ' * (largura - 2) + '*')
if altura > 1:
    print('*' * largura)

                      
    
    
