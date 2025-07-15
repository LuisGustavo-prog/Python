def higher_and_lower(value):
    list0f = max(value)
    list0F = min(value)

    for i in value:
        if i == list0f:
            print(f'O maior número é: {i}')
        elif i == list0F:
            print(f'O menor número é: {i}')
        else:
            print(f'Os número intermediarios: {i}')
    

higher_and_lower([10, 5, 2])