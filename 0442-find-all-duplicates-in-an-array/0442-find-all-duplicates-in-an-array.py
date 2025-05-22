class Solution(object):
    def findDuplicates(self, nums):
        from collections import Counter
        count = Counter(nums)
        return [num for num in count if count[num] == 2]