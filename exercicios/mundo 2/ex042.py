n1 = int(input('Digite o primeiro segmento: '))
n2 = int(input('Digite o Segundo segmento: '))
n3 = int(input('Digite o Terceiro segmento: '))

if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    if n1 == n2 == n3:
        print('Equilatero')
    elif n1 != n2 != n3 != n1:
        print('Escaleno')
    else:
        print('Isósceles') 
else:
    print('Não se pode formar uma triângulo')