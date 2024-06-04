class Solution(object):
    def isPalindrome(self, s):
        s=s.lower()
        st=""
        if(len(s)==0):
            return True
        else:
            for i in s:
                if(i.isalnum()):
                    st=st+i
        return st[::-1]==st
                