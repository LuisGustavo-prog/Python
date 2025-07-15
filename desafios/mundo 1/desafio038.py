def people_with_age_drink(age):
    if age <= 16:
        return 'drink toddy'
    elif age == 17:
        return 'drink coke'
    elif age <= 20:
        return 'drink beer'
    elif age >= 21:
        return 'drink beer'
    elif age >= 30:
        return 'drink whisky'
    

print(people_with_age_drink(17))