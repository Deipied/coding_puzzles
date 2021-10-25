# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def addTwoNumbers(l1,l2):
    while len(l1) > len(l2):
        l2.append(0)
    while len(l2) < len(l2):
        l1.append(0)
    carry = 0
    ans = []
    for i in range(len(l1)):
        sum = carry + l1[i] + l2[i]
        if sum > 9:
            ans.append(sum - 10)
            carry = 1
            if i == len(l1)-1:
                ans.append(1)
        else:
            ans.append(sum)
            carry = 0
    return ans

l1 = [9,9,9,9]
l2 = [9,9]
print(addTwoNumbers(l1,l2))
