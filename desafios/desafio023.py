name =  str(input('Digite seu nome: '))
print(name.upper())
print(name.lower())

sem_espaço = name.replace(' ', '')
print(sem_espaço)
print(name, len(sem_espaço))

primeiro_nome = name.split()
print(primeiro_nome)
print(len(primeiro_nome[0])) 

