
meses_nomes = {
    1: 'Janeiro',
    2: 'Fevereiro',
    3: 'Março',
    4: 'Abril',
    5: 'Maio',
    6: 'Junho',
    7: 'Julho',
    8: 'Agosto',
    9: 'Setembro',
    10: 'Outubro',
    11: 'Novembro',
    12: 'Dezembro'
}


dia = int(input('Digite o dia do seu nascimento: '))
mes_numero = int(input('Digite o seu mês de nascimento (em número): '))
ano = int(input('Digite o seu ano de nascimento: '))


nome_do_mes = meses_nomes.get(mes_numero, 'Mês Inválido')


print(f'{dia} de {nome_do_mes} de {ano}')




