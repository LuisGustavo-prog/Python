# print('-------- Parcelador automático --------')
# n1 = float(input('Digite o número da divida: '))
# n2 = int(input('Digite o número de parcelas desejadas: '))
# resultado = (n1 / n2)
# print('Você tem essa é a quantia a pagar: {:.2f}'.format(resultado))

print('-------- Parcelador automático --------')
print('Parcelas a cima de 6 vão estar sujeitas a uma taxa de 5% de juros, e acima de 12 o juros aumenta pra 15%.')
n1 = float(input('Digite o número da divida: '))
n2 = int(input('Digite o número de parcelas desejadas: '))
if n2 <= 5:
    resultado = n1 / n2
    print('Essa é a quantia a pagar: R${:.2f}'.format(resultado))
elif n2 >= 6 and n2 < 12:
    juros = 5 / 100 # pra descobrir o número decimal.
    resu = n1 * (1 + juros)
    parcela_com_juros = resu / n2
    print('Essa é a quantia a pagar com 5% de juros: R${:.2f}'.format(parcela_com_juros))
elif n2 >= 12:
    juros1= 15 / 100 # pra descobrir o número decimal.
    resu1 = n1 * (1 + juros1)
    parcela_com_juros1 = resu1 / n2
    print('Essa é a quantia a pagar com 15% de juros: R${:.2f}'.format(parcela_com_juros1))
else:
    print('se burro')
