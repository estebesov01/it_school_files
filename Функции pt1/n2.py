# Создайте функцию которая генерирует 10 чисел Фибоначчи: 
# 1,1,2,3,5,8,13,21,34,...
fib_list = []
a, b = 0, 1
for _ in range(10):
    fib_list.append(a)
    a, b = b, a + b
print(fib_list)