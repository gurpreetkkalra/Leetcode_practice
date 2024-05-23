class Solution(object):
    def strStr(self, haystack, needle):
        if needle not in haystack:
            return -1
        else:
            index=haystack.index(needle)
        return index