# def findMedianSortedArrays(nums1, nums2):
#     p1 = 0
#     p2 = 0
#     ans = []
#     while p1 <= len(nums1) - 1 and p2 <= len(nums2) - 1:
#         if nums1[p1] == nums2[p2]:
#             ans.append(nums1[p1])
#             ans.append(nums2[p2])
#             p1 += 1
#             p2 += 1
#         elif nums1[p1] < nums2[p2]:
#             ans.append(nums1[p1])
#             p1+= 1
#         elif nums1[p1] > nums2[p2]:
#             ans.append(nums2[p2])
#             p2+= 1
        
#         if p1 == len(nums1) - 1 and p2 < len(nums2) - 1:
#             while p2 < len(nums2):
#                 ans.append(nums2[p2])
#                 p2 += 1
#         elif p2 == len(nums2) - 1 and p1 < len(nums1) - 1:
#             while p1 < len(nums1):
#                 ans.append(nums1[p1])
#                 p1 += 1
#     if len(ans)%2 == 0:
#         return (ans[len(ans)/2]+ans[(len(ans)/2)-1])/2
#     else:
#         return ans[math.ceil(len(ans)/2)]
        
        
nums1 = [1,2]
# nums2 = [3,4]
print(len(nums1))