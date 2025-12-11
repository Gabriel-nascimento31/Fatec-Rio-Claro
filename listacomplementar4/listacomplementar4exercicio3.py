nomes = ['anderson', 'rute', 'gustavo', 'julia', 'rafael']
usuario = input('Digite o nome de uma pessoa para verificar se está na lista: ').lower()
if usuario in nomes:
    print('ESSE NOME ESTÁ NA LISTA ')
else:
    print('ESSE NOME NÃO ESTÁ NA LISTA ')
    