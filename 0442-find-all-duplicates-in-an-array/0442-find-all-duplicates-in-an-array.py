class Solution(object):
    def findDuplicates(self, nums):
        lst = []
        s = set()
        for num in nums:
            if num in s and num not in lst:
                lst.append(num)
            else:
                s.add(num)
        return lst