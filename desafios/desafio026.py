name = str(input('Digite seu nome: '))

if name.find('Silva'):
    print('Seu nome tem Silva!')
elif name.find('silva'):
    print('Seu nome tem silva!')
else:
    print('Seu nome não tem silva')