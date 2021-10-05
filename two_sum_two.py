def twoSum(numbers, target):
    p1 = len(numbers)-1
    while p1 > 0:
        for p2 in range(len(numbers)-2,-1,-1):
            if numbers[p1]+numbers[p2] == target:
                return [p2+1, p1+1]
            elif p2 == 0:
                numbers.pop(len(numbers)-1)
                p1 -= 1













numbers = [2,7,11,15]
target = 9
print(twoSum(numbers, target))