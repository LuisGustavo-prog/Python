import datetime

dt = datetime.datetime.today().year

def idade(nascimento, ano_atual):
    birth = nascimento - ano_atual
    return abs(birth)

birth = idade(2009, dt)

difference = abs(birth - 18)

if birth < 18:
    if birth == 17:
        print('Com base na sua idade de {} anos,  O alistamento militar ainda deverá ser agendado até o ano que vem.'.format(birth))
    elif birth <= 16:
        print('Com base na sua idade de {} anos,  O alistamento militar ainda deverá ser agendado até daqui {} anos.'.format(birth, difference))
elif birth == 18:
    print('Você deverá comparecer ao alistamento militar.')
else:
    print('Seu comparecimento ao alistamento militar requisitado, pois, você não compareceu aos 18 anos. Contagem de anos atrasado: {} anos'.format(difference))

