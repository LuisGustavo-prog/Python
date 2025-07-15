import datetime

current_year = datetime.datetime.today().year
birth = 2014

result_birth = abs(current_year - birth)

if result_birth <= 9:
    print('Sua categoria é mirim!')
elif result_birth > 9 and result_birth <= 14:
    print('Sua categoria é infatil!')
elif result_birth > 14 and result_birth <= 19:
    print('Sua categoria é junior!')
elif result_birth == 20:
    print('Sua categoria é Sénior!')
else:
    print('Sua categoria é Master!')
