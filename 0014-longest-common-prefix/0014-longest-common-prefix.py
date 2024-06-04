class Solution(object):
    def longestCommonPrefix(self,strs):
        smallest_word = min(strs, key=len)
        for i in range (len(smallest_word)):
            for j in strs:
                if (j[i]!=smallest_word[i]):
                    return smallest_word[:i]
        return smallest_word

        
            
            
        