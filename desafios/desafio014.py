salario = float(input('Digite o valor do seu salário atual: R$'))
porcentagem = int(input('Digite o quanto você quer de aumento: '))
novo = (salario * porcentagem / 100) + salario # Primeiro valor é o número cheio e o segundo é pra porcentagem
print('Seu salário foi ajustado com um bonus de {}%, confira seu novo salário: R${:.2f}.'.format(porcentagem, novo))
