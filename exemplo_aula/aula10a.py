name = str(input('Digite seu nome: '))
if name == 'Gustavo':
    print('Que nome lindo você tem!')
else:
    print('Não gostei do seu nome!')
print('Bom dia, {}!'.format(name))

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('A sua média foi {:.1f}'.format(m))
if m >= 6.0:
    print('Sua média foi boa, parabéns!')
else:
    print('Sua média está podre!')