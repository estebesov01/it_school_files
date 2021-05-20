# Напишите функцию которая 
# принимает 2 Dictionary и 
# добавляет втрорую Dictionary к первой.


def addDict(first,second):
    first.update(second)
    return first

dict1 = {
    1:'one',
    2:'two',
    3:'three',
    4:'four',
    5:'five',
}
dict2 = {
    6:'six',
    7:'seven',
    8:'eight',
    9:'nine',
}
print(addDict(dict1, dict2))