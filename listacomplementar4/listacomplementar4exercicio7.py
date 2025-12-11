def contar_vogais(frase):
    
    vogais = 'aeiouáéíóúãõâêîôû'

    contador = 0

    frase_min = frase.lower()

    for caractere in frase_min:
        
        if caractere in vogais:
            contador = contador + 1

    return contador


frase_usuario = input('Digite uma frase: ')


total_vogais = contar_vogais(frase_usuario)


print(f'A frase {frase_usuario} possui {total_vogais} vogais')


