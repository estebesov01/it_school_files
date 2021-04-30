nums = [1,2,3,1,2,5,6]
for i in range(len(nums)-1):
    for j in nums:
        if i == nums[j]:
            nums.remove(i)
print(nums)