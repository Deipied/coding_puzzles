def moveZeroes(nums):
    count = 0
    if len(nums) == 1 and nums[0] == 0:
        return nums
    for i in range(len(nums)-1,-1,-1):
        if nums[i] == 0:
            nums.pop(i)
            count += 1
    while count > 0:
        nums.append(0)
        count -= 1
    return nums



nums = [0,1,0,3,12]
print(moveZeroes(nums))