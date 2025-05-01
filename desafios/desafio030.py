def fine(km):
    if km <= 80:
        print('Você não recebeu nenhuma multa.')
    elif km >= 81:
        result = abs((80 - km) * 7)
        print('Total a pagar em multa R${}'.format(result))
        return result
    else:
        print('Digite um valor valido.')
 
fine(120)