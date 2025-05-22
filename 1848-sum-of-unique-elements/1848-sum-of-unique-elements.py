class Solution(object):
    def sumOfUnique(self, nums):
        sum = 0
        lst = []
        for i in range (len(nums)):
            if nums.count(nums[i]) == 1:
                sum += nums[i]
        return sum
