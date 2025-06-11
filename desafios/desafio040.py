number = 124342

def type_numbers(choice, number):
    if choice.lower() == 'a':
        return bin(number)
    elif choice.lower() == 'b':
        return oct(number)
    else:
        return hex(number)


print(type_numbers('A', 1290))