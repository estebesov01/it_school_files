
n2 = "У вас есть строка 'Запуск Ethereum 2.0 состоится 1 декабря. На депозитный контракт внесено более 524 288 ETH'".split()
for i in n2:
    print(i,type(i))
n3 = 'хакеры слили в сеть данные пакистанской энергетической компании k-Electric'.title()
print(n3)
n4 = 'GitHub'
sss = input("Введите символ разделитель : ")
print(n4.split(sss))
n5 = 'Ботнет IPStorm , в который ранее входили лишь Windows-машины, увеличился до 13 500 зараженных систем'.replace('е','3')
print(n5)
n6 = input("Введите предложение : ")
print(n6[:int(len(n6)/2)].lower()+n6[int(len(n6)/2):].upper())
n7 = True
print(str(n7))