salario = float(input('Digite o valor do seu salário atual: R$'))
novo = (salario * 15 / 100) + salario
print('Seu salário foi ajustado com um bonus de 15%, confira seu novo salário: R${:.2f}.'.format(novo))
