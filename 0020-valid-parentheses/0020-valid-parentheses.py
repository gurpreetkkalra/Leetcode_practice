class Solution(object):
    def isValid(self, s):
        stack = []
        parantheses = {')':'(', '}':'{' ,']':'['}

        for i in s:
            if i in '({[':
                stack.append(i)
            elif i in ')}]':
                if not stack or stack[-1] != parantheses[i]:
                    return False
                stack.pop()

        return len(stack)==0
