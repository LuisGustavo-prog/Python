import math

an = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(an))
print('O angulo de {} tem o seno de {:.2}'.format(an, seno))
cosseno = math.cos(math.radians(an))
print('o angulo de {} tem o cosseno de {:.2f}'.format(an, cosseno))
tangente = math.tan(math.radians(an))
print('o angulo de {} tem a tangente de {:.2f}'.format(an, tangente))
