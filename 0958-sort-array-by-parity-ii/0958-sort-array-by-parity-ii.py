class Solution(object):
    def sortArrayByParityII(self, nums):

        arr = []

        even = []
        odd = []

        for num in nums:
            if (num % 2 == 0):
                even.append(num)
            else:
                odd.append(num)
        
        for i in range(len(nums)//2):
            arr.append(even[i])
            arr.append(odd[i])
        
        return arr