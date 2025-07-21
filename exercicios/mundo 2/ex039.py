from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = abs(atual - nasc)
sexo = input('digite seu sexo: ')
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))

if sexo.lower() == 'masculino' or sexo == 'homem':
    if idade == 18:
        print('Você tem que se alistar IMEDIATAMENTE!')
    elif idade < 18:
        saldo = abs(idade - 18)
        print('Você ainda não tem 18 anos. Ainda faltam {} anos para o alistamento.'.format(saldo))
    elif idade > 18:
        saldo = abs(idade - 18)
        print('Você já deveria ter se alistado há {} anos.'.format(saldo))
else:
    print('Você não pode se alistar.')
    