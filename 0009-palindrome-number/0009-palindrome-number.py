class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        n = x
        sum = 0
        while n != 0:
            rem = n%10
            sum = sum*10 + rem
            n = n//10
        return sum == x
        