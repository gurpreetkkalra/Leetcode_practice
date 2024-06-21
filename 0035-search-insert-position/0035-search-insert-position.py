class Solution(object):
    def searchInsert(self, nums, target):
        for i in range (len(nums)):
            if (nums[i]==target):
                return i
        for j in range (len(nums)):
            if (nums[-1]<=target):
                return len(nums)
            elif (nums[j]<=target):
                continue
            else:
                return j
        