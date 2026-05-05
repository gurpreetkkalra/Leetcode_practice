class Solution(object):
    def isPalindrome(self, s):
        result = ""
        for char in s:
            if char.isalnum():
                result+=char
        r = result.lower()
        if (r[::-1] == r):
            return True
        else:
            return False
        