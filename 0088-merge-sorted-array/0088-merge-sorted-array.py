class Solution(object):
    def merge(self, nums1, m, nums2, n):

        merged = []

        i = 0
        j = 0
        k = 0

        while i < m and j < n:
            if (nums1[i] <= nums2[j]):
                merged.append(nums1[i])
                i+=1
            else:
                merged.append(nums2[j])
                j+=1

        while i < m:
            merged.append(nums1[i])
            i+=1

        while j < n:
            merged.append(nums2[j])
            j+=1

        for k in range (m + n):
            nums1[k] = merged[k]

        return nums1


            
    
            
            
        