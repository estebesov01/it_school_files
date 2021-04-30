import random
cnt = 0
for i in range(10):
    a = random.randint(0,10)
    b = random.randint(0,10)
    answer = int(input(f"{a} * {b} = "))
    if answer == a * b:
        cnt+=1
print(f"Ваш результат : {cnt*10}%")