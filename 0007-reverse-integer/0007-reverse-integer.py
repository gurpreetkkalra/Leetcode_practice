class Solution(object):
    def reverse(self, x):
        s=str(x);
        if(s[0]!=0 and s[0]!='-'):
            answer=int(s[::-1])
        else:
            answer= int('-'+s[:0:-1])
        if answer<-2**31 or answer> 2**31 - 1:
            return 0
        return answer