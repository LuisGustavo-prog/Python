def Bank(house, salary, months):
    installment_value = house / months
    percentage = (30 / 100) * salary

    if installment_value > percentage:
        return 'O empréstimo foi negado.'
    elif installment_value <= percentage:
        return 'O empréstimo foi aprovado!'


print(Bank(3000, 1200, 12))
