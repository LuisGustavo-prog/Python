n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2 
di = n1 // n2
e = n1 ** n2
print('A soma é {}, o produto é {} e a divisão é {:.3f}' .format(s, m, d), end=' ') # O {:.3f} serve pra que a divisão nã tenha uma alta repetição nos números, ai você decide o quanto de número que você quer só mudando o 3.
print('Divisão inteira {} e potência {}'.format(di, e))
