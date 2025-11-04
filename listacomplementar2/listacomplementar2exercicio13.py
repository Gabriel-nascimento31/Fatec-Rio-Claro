print('--- Caixa eletrônico ---')

valor_saque = -1

while valor_saque != 0:
    valor_saque = int(input('\nDigite um valor inteiro para sacar, caso queira encerrar o programa digite 0: '))
    if valor_saque == 0:
        print('\nObrigado por utilizar o serviço. Até logo! ')
        break
    elif valor_saque < 0:
        print('Valor inválido. Digite um valor positivo. ')
        continue
    print(f'\nDecomposição de R${valor_saque:.2f}: ')

    restante = valor_saque


    # === 2. Lógica de Decomposição (Notas) ===
    # -----------------------------------------
    # NOTA R$ 100,00
    quantidade_100 = restante // 100
    if quantidade_100 > 0:
        print(f'- {quantidade_100} nota(s) de R$ 100.00')
        restante = restante % 100

    # ------------------------------------------------
    # NOTA R$ 50,00
    quantidade_50 = restante // 50
    if quantidade_50 > 0:
        print(f'- {quantidade_50} nota(s) de R$ 50.00')
        restante = restante % 50

    # ------------------------------------------------
    # NOTA R$ 20,00
    quantidade_20 = restante // 20
    if quantidade_20 > 0:
        print(f'- {quantidade_20} nota(s) de R$ 20.00')
        restante = restante % 20

    # --------------------------------------------------
    # NOTA R$ 10,00
    quantidade_10 = restante // 10
    if quantidade_10 > 0:
        print(f'- {quantidade_10} nota(s) de R$ 10.00')
        restante = restante % 10

    # ---------------------------------------------------
    # NOTA R$ 5,00
    quantidade_5 = restante // 5
    if quantidade_5 > 0:
        print(f'- {quantidade_5} nota(s) de R$ 5.00')
        restante = restante % 5

    # ----------------------------------------------------
    # NOTA R$ 2,00
    quantidade_2 = restante // 2
    if quantidade_2 > 0:
        print(f'- {quantidade_2} nota(s) de R$ 2.00')
        restante = restante % 2

    # --------------------------------------------------------
    # NOTA R$ 1,00
    quantidade_1 = restante // 1
    if quantidade_1 > 0:
        print(f'- {quantidade_1} nota(s) de R$ 1.00')
        restante = restante % 1
        
        
