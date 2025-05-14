class Solution(object):
    def sortArrayByParity(self, nums):
        arr = []
        j = 0

        for num in nums:
            if(num %2 == 0):
                arr.append(num)
        for num in nums:
            if(num %2 != 0):
                arr.append(num)

        return arr
