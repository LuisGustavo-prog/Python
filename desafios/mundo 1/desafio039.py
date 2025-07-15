# Buy = int(input('Digite o valor do \033[31mimovel:\033[m '))
# salary = int(input('Digite o valor do seu \033[31msalario: \033[m'))
# years = int(input('Digite o valor de anos que você deseja \033[31mpagar: \033[m'))
salary = 1000
buy = 2000
years = 7

ploats = buy / years
percentage = (30 / 100) * salary

if ploats <= percentage:
    print('Parabéns! A compra do seu imovel foirealizada com sucesso.')
else:
    print('infelizmente a compra não foi aprovada.')