# def findMedianSortedArrays(nums1, nums2):
        if len(nums1) == 0:
            return median(nums2)
        if len(nums2) == 0:
            return median(nums1)
        p1 = 0
        p2 = 0
        ans = []
        tlen = len(nums1) + len(nums2)
        target_index = tlen/2
        index = 0
        while target_index != index and p1 != len(nums1) and p2 != len(nums2):
            if nums1[p1] == nums2[p2]:
                ans.append(nums1[p1])
                index += 1
                p1 += 1
                ans.append(nums2[p2])
                p2 += 1
                index += 1
            elif nums1[p1] < nums2[p2]:
                ans.append(nums1[p1])
                index += 1
                p1+= 1          
            elif nums1[p1] > nums2[p2]:
                ans.append(nums2[p2])
                index += 1
                p2+= 1
        while p1 == len(nums1):
            ans.append(nums2[p2])
            p1 += 1
        while p2 == len(nums2):
            ans.append(nums1[p1])
            p2 += 1
        if tlen%2 == 0:
            return (ans[index] + ans[index-1])/2
        else:
            return ans[index]

# having a problem where I am constantly switching values between target index and  p1 an p2 values
# current code problem is with not being able to do [1,3] and [2], because it adds 3 instead of ending with 2
# its because of my two while statements, which handles cases where you need to add another value