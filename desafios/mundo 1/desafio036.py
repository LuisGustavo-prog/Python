def Triangle(a, b, c):
    sum_a = a + b
    sum_b = a + c
    sum_c = b + c
    if sum_a > c:
        if sum_b > b:
            if sum_c > a:
                print('É possível fazer um triângulo com os valores passados.')
            else:
                print('Não é possível criar um triângulo com esses valores.')
        else:
            print('Não é possível criar um triângulo com esses valores.')
    else:
        print('Não é possível criar um triângulo com esses valores.')


Triangle(2, 3, 4)