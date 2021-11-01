def findDuplicate(nums):
    if len(nums) == 1:
        return False
    ans = {}
    for i in range(len(nums):
        if nums[i] in ans:
            return True
        else:
            ans[nums[i]] = 1
    return False

nums = [1,2,3,4,1]
print(findDuplicate(nums))