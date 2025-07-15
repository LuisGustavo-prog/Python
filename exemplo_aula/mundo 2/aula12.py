nome = str(input('Qual seu nome?'))

if nome == 'Gustavo':
    print('Que nome bonito!')
elif nome == 'pedro' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana':
    print('Um belo nome feminino.')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))