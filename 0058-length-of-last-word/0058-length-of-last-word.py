class Solution(object):
    def lengthOfLastWord(self, s):
        a = s.split()[-1]
        return len(a)

        