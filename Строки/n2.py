# Взять строку №8 и поделить 
# её по пробелам и узнать тип 
# данных каждого слова.
n2 = "У вас есть строка 'Запуск Ethereum 2.0 состоится 1 декабря. На депозитный контракт внесено более 524 288 ETH'".split()
for i in n2:
    print(i,type(i))