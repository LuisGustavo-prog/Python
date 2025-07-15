def year(a):
    import datetime

    year = datetime.date.today().year
    result = abs(2005 - year)
    teste = abs(result - 18)

    if result == 17:
        return f'É a hora de se alistar'
    elif result <= 16:
        return f'Você ainda vai se alistar, {teste} Falta isso de anos'
    else:
        return f'Já passou da hora de você se alistar, {teste} Já passou isso de anos'

print(year(18))