class Solution(object):
    def plusOne(self, digits):
        new_digits=[]
        digits=str(digits)
        st=""
        for i in digits:
            if(i.isalnum()):
                st+=i
        new_num=int(st)+1
        for digit in str(new_num):
            new_digits.append(int(digit))
        return new_digits