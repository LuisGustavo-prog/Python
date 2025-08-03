from datetime import date

atual = date.today().year
nascimento = int(input('Ano de Nascimento: '))
idade = abs(atual - nascimento)
print(f'O atleta tem {idade} anos.')

if idade <= 9:
    print('Classificação: MIRIM')
elif idade > 9 and idade <= 14:
    print('Classificação: INFATIL')
elif idade > 14 and idade <= 19:
    print('Classificação: JUNIOR')
elif idade > 19 and idade <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')

# Fazendo de outra maneira, essa maneira é mais eficiente, pois, eu vou cortar algumas coisas, mas terá o mesmo resultado.

if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14: # Eu tirei o "and" porque se ele for maior que 9, então ele já passou da primeira condição, eu não preciso colocar de "elif idade > 9 and idade <= 14:" por que ele já passou da primeira condição.
    print('Classificação: INFATIL')
elif idade <= 19:
    print('Classificação: JUNIOR')
elif idade <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')