car = int(input('Digite o número de dias com o carro alugado: '))
km = float(input('Digite o número de km rodados: '))
n1 = car * 60
n2 = (km * 0.15) + n1
print('Total a pagar é de R${:.2f}'.format(n2))
