def Bank(house, salary, months):
    installment_value = house / (months * 12)
    percentage = salary *  (30 / 100)

    if installment_value > percentage:
        return 'O empréstimo foi negado.'
    elif installment_value <= percentage:
        return 'O empréstimo foi aprovado!'


print(Bank(80000, 10000, 7))