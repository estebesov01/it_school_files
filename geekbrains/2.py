import random, math
#1
fruits = ["яблоко","банан","киви","арбуз"]
j = 1
for i in fruits:
    print(f"{j}." + "{:>6}".format(i))
    j+=1
#2
list1 = [1,2,3,4,5,6,7,8,9]
list2 = [2,4,6,7,9]
list1 = set(list1)-set(list2)
print(list1)
#3
someList = [x for x in range(10)]
someList1 = [i / 4 if i % 2 == 0 else i * 2 for i in someList]
print(someList1)
#4
List1 = [random.randint(0,100) for x in range(10)]
print(List1)
List2 = [int(math.sqrt(i)) for i in List1 if math.sqrt(i) % 1 == 0]
print(List2)
#5
