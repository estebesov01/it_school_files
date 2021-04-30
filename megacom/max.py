num = int(input("Введите целое: "))
num1 = num
sum = 0
nums = []
while (num != 0):
    nums.append(num%10)
    num = num // 10
print(f"Наибольшая цифра в числе {num1} = {max(nums)}")