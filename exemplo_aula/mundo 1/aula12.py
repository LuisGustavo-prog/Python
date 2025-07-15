name = str((input('Digite seu \033[4;31mnome:\033[m')))

if name == 'Gustavo':
    print('Que nome bonito!')
elif name == 'Pedro' or name == 'Maria' or name == 'Paulo':
    print('Seu nome é bem popular no Brasil.')
elif name in 'ana cladiua jessica juliana':
    print('Você tem um nome muito bonito.')
print('Tenha um bom dia, {}'.format(name))
