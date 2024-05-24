class Solution(object):
    def twoSum(self, nums, target):
        hmap={}
        for i in range(len(nums)):
            dif=target-nums[i]
            if dif in hmap:
                return [hmap[dif],i]
            hmap[nums[i]]=i
        return
                