class Solution(object):
    def mergeArrays(self, nums1, nums2):
        result = {}

        for key, val in nums1:
            if key in result:
                result[key] +=val
            else:
                result[key] = val


        for key, val in nums2:
            if key in result:
                result[key] +=val
            else:
                result[key] = val

        merged = []

        for key in sorted(result):
            merged.append([key, result[key]])
        
        return merged


        
        