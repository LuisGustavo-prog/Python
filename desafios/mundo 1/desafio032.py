def price(pay):
    if pay <= 200:
        resutl = pay * 0.50
        print('O preço da sua passagem ficou R${:.2f}'.format(resutl))
    else:
        resutl = pay * 0.45
        print('O preço da sua passagem ficou R${:.2f}'.format(resutl))

price(50)