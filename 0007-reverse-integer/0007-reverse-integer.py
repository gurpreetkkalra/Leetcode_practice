class Solution(object):
    def reverse(self, x):
        if x < 0:
            sign = -1
        else: 
            sign = 1
        
        rev = sign * int(str(abs(x))[::-1])
        if rev < -2 ** 31 or rev > 2**31 -1:
            return 0
        return rev
        