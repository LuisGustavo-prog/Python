city = input('Digite o nome da sua cidade: ')
lista = city.split()

if 'Santo' in lista[0]:
    print('O nome da sua cidade começa com santo.')
elif 'santo' in lista[0]:
    print('O nome da sua cidade começa com santo.')
else:
    print('O nome da sua cidade não começa com santos.')