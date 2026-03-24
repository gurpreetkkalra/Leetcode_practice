class Solution(object):
    def scoreOfString(self, s):
        a = 0
        for i in range (1,len(s)):
            a += abs(ord(s[i-1])- ord(s[i]))
        return a