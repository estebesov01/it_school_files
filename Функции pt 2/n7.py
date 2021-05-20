# Создайте функцию которая принмает 
# тип данных dictionary, но возвращает 
# два Tuple в одном из них все ключи, в 
# другом только значения.
def tuplemake(somedict):
    keytuple = tuple(somedict.keys())
    valuetuple = tuple(somedict.values())
    return keytuple, valuetuple


somedict = {
    1:'bir',
    2:'eki',
    3:'uch',
}
a, b = tuplemake(somedict)
print(a)
print(b)