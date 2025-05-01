def calculador_de_imposto(valor_do_produto, parcelas):
    if parcelas <= 5:
        resultado_final = valor_do_produto / parcelas
        print('Resultado final sem juros: {:.2f}'.format(resultado_final))
    elif 6 <= parcelas <= 12:
        resultado_final = 5 / 100
        resultado_final_com_juros = valor_do_produto * (1 + resultado_final)
        print('Resultado final com 5% de juros: {:.2f}'.format(resultado_final_com_juros))
    elif 13 <= parcelas <= 23:
        resultado_final = 15 / 100
        resultado_final_com_juros = valor_do_produto * (1 + resultado_final)
        print('Resultado final com 15% de juros: {:.2f}'.format(resultado_final_com_juros))
    elif parcelas >= 24:
        resultado_final = 20 / 100
        resultado_final_com_juros = valor_do_produto * (1 + resultado_final)
        print('Resultado final com 20% de juros: {:.2f}'.format(resultado_final_com_juros))
    else:
        print('burro')



print('-------- Parcelador automático --------')
print('Parcelas a cima de 6 vão estar sujeitas a uma taxa de 5% de juros, e acima de 12 o juros aumenta pra 15%, acima de 24 o juros aumenta sobe para 20%.')
n1 = float(input('Digite o número da divida: '))
n2 = int(input('Digite o número de parcelas desejadas: '))   
resultado = calculador_de_imposto(n1, n2) 
