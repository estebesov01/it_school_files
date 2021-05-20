dict_ = {'name': 'john', 'lastname': 'Snow', 12: 'age'}
try:
    for x in dict_.keys():
        x + 'abc'
except TypeError:
    print('Непральна у вас чето')