class Solution(object):
    def findIntersectionValues(self, nums1, nums2):
        count1 = 0
        count2 = 0
        n = len(nums1)
        m = len(nums2)
        for i in range(n):
            if nums1[i] in nums2:
                count1 += 1
        
        for j in range (m):
            if nums2[j]in nums1:
                count2 += 1

        return[count1, count2]