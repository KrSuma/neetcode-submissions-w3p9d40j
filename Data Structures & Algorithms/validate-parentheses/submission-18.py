class Solution:
    def isValid(self, s: str) -> bool:
        
        closing = {')':'(', ']':'[', '}':'{',}
        stack = []


        for c in s:
            if c in closing:
                if stack and closing[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False