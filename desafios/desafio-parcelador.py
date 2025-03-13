def calculador_de_imposto(valor_do_produto, parcelas):
    match parcelas:
        case x if x <= 5:
            resultado_final = valor_do_produto / parcelas
            print(f"Resultado final sem juros: {resultado_final}")
        
        case x if 6 >= 12:
            resultado_final = 5 / 100
            resultado_final_com_juros = valor_do_produto * (1 + resultado_final)
            print(f"Resultado final com 5% de juros: {resultado_final_com_juros}")
        
        case x if 13 >= 23:
            resultado_final = 15 / 100
            resultado_final_com_juros = valor_do_produto * (1 + resultado_final)
            print(f"Resultado final com 15% de juros: {resultado_final_com_juros}")
        
        case x if x > 24:
            resultado_final = 20 / 100
            resultado_final_com_juros = valor_do_produto * (1 + resultado_final)
            print(f"Resultado final com 20% de juros: {resultado_final_com_juros}")
        
        case _:
            print('Digite uma resposta válida.')


print('-------- Parcelador automático --------')
print('Parcelas a cima de 6 vão estar sujeitas a uma taxa de 5% de juros, e acima de 12 o juros aumenta pra 15%, acima de 24 o juros aumenta sobe para 20%.')
n1 = float(input('Digite o número da divida: '))
n2 = int(input('Digite o número de parcelas desejadas: '))   
resultado = calculador_de_imposto(n1, n2)   
