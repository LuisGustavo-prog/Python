import random
from time import sleep

print('-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=')
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=')
number = int(input('Em que número eu pensei?')) # O jogador tenta adivinhar
print('Processando...')
sleep(3) # Dá um time, é como se o computador estivesse pensando

number_random = random.randint(0, 5) #
if number == number_random:
    print('Parabéns, você acertou o número!!!')
else:
    print('Infelizmente você não acerou o número!!!')
