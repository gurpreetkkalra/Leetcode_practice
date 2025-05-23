class Solution(object):
    def areOccurrencesEqual(self, s):
        count = {}
        for char in s:
            if char in count:
                count[char] +=1
            
            else:
                count[char] = 1

            values = list(count.values())

        if(len(set(count.values())) != 1):
            return False
            
        else:
            return True


