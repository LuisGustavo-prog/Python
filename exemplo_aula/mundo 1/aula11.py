print('\033[1;31;43mOlá, mundo!\033[m')

print('\033[4:30;45mOlá, mundo \033[m')

print('\033[7;30mOlá, mundo \033[m')

a = 3
b= 5
print('Os valores são \33[32m{}\033[m e \033[31m{}\033[m'.format(a, b))

# Adicionando cores usando o .format
name = 'guanabara'
print('Olá! muito prazer em te conhecer, {}{}{}!!!'.format('\033{4;34m', name, '\033{m'))

# Adicionando cores usando um dicionario
name = 'guanabara'
color = {'Clear':'\033[m', 
         'Blue':'\033[34m', 
         'Yellow':'\033[33m', 
         'blackwhite':'\033[7;30m'}
print('Olá! muito prazer em te conhecer, {}{}{}!!!'.format(color['Yellow'], name, color['Clear']))

# \033[0;30;41m
     
# \033[4;33;44m
     
# \033[0;30;41m

# \033[1;35;43m

# \033[30;42m

# \033[m

# \033[7;30m