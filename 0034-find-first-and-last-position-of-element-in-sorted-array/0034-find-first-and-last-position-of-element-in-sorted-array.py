class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        pos=-1
        position=-1
        for i in range (len(nums)):
            if(nums[i]==target):
                pos=i
                break
            else:
                pos=-1
        
        for i in range(len(nums)-1,-1,-1):
            if(nums[i]==target):
                position=i
                break
            else:
                position=-1
        return [pos,position]
                