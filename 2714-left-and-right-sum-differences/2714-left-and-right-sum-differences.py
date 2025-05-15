class Solution(object):
    def leftRightDifference(self, nums):
        leftSum = []
        rightSum = []

        leftSum.append(0)
        for i in range (len(nums)-1):
            leftSum.append(nums[i] + leftSum[i])

        
        rightSum = [0] * len(nums)
        for j in range(len(nums) - 2, -1, -1):
            rightSum[j] = rightSum[j + 1] + nums[j + 1]

        arr = []

        for k in range(len(nums)):
            arr.append(abs(leftSum[k] - rightSum[k]))
        
        return arr
            
