def calculatio(num):
    if num >= 1200:
        # resutl = num + (10 / 100) * num Caso eu queria já fazer o total do salário desse macho aqui.
        resutl = num + (10 / 100) * num
        print('Seu teve um bônus de 10% no aumento salarial R${:.2f}'.format(resutl))
    else:
        resutl = num + (15 / 100) * num
        print('Seu teve um bônus de 15% no aumento salarial R${:.2f}'.format(resutl))

calculatio(1500)