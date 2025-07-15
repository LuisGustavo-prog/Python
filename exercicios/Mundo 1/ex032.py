import datetime

ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = datetime.date.today().year # Pega o ano atual da sua máquina
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0: #  Cálculo para descobrir se o ano é bissexto
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} NÃO é BISSEXTO'.format(ano))