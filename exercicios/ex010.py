real = float(input('Digite um número para conversão: R$'))
dolar = real / 5.79
euro = real / 6.27
print('com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))
print('com R${:.2f} você pode comprar EUR{:.2f}'.format(real, euro))
