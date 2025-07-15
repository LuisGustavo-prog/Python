def bissexto(num):
    if num % 4 == 0:
        if num % 100 != 0 or num % 400 == 0:
            print('O ano é bissexto.')
        else:
            print('O ano não é bissexto.')
    else:
        print('O ano não é bissexto.')

bissexto(2020)
