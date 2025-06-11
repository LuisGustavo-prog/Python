def triangle(a, b, c):
    if a == b and a == c:
        return 'Equilátero: Todos os lados são iguais.'
    elif a != b and a == b or b != a and b == c or c != b and c == a:
        return 'Isósceles: Dois lados são iguais.'
    else:
        return 'Escaleno: Todos os lados são diferentes.'
    
print(triangle(1,2,3))