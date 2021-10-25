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

# Two pointer solutoin with one looping through and another pos looping through separately switching indices
# class Solution:
#     def moveZeroes(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: void Do not return anything, modify nums in-place instead.
#         """
#         pos = 0
        
#         for i in range(len(nums)):
#             el = nums[i]
#             if el != 0:
#                 nums[pos], nums[i] = nums[i], nums[pos]
#                 pos += 1



nums = [0,1,0,3,12]
print(moveZeroes(nums))