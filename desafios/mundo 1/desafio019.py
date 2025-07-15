import math
ângulo = int(input('Digite o número seno: '))
seno = math.sin((math.pi / 180) * ângulo)
cosseno = math.cos((math.pi / 180) * ângulo)
tangete = math.tan((seno / cosseno))
print('O valor em seno {}, em consseno {}, em tangete {}.'.format(seno, cosseno, tangete))
