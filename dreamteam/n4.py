def somefunc(someset,i):
    someset = list(someset)
    print(someset[i])
    if i == 0:
        return
    somefunc(someset,i - 1)


data_set = {('login', 'password', 'codeword'), 1988, 32, 'Python', 'Kyrgyzstan', ('October', 'November', 'December'), 'Senior', 'TeamLead'}
somefunc(data_set,len(data_set) - 1)