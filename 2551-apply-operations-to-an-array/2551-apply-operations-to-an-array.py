class Solution(object):
    def applyOperations(self, nums):
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
        result = []
        for j in range(len(nums)):
            if nums[j] != 0 :
                result.append(nums[j])
        while len(result) < len(nums):
            result.append(0)
                
        return result
