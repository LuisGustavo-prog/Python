def imc(height, kg):
    imc = kg / (height ** 2) 

    if imc < 18.5:
        return 'Abaixo do peso'
    elif imc >= 18.5 and imc <= 25:
        return 'Peso ideal'
    elif imc > 25 and imc <= 30:
        return 'Sobrepeso'
    elif imc > 30 and imc <= 40:
        return 'Obesidade' 
    else:
        return 'Obesidade Mórbida'