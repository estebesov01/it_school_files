import random
nums = [random.randint(0,1000) for i in range(1000)]
nums1 = []
for i in nums:
    if i % 2 == 0:
        nums1.append(i)
print(len(nums1))